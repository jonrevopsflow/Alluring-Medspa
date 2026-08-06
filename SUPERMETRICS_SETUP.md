# Supermetrics Integration Guide - IVitamin Dashboard

## Overview
This guide connects your Supermetrics Google Ads data to the IVitamin dashboard with automated daily refresh.

---

## Step 1: Get Your Supermetrics API Key

### Option A: Use Existing Supermetrics Account
1. Log into **Supermetrics** (supermetrics.com)
2. Go to **Settings → API Keys**
3. Click **"Create New API Key"** (or use existing)
4. Copy your **API Key** (you'll need this)

### Option B: Create New Supermetrics Account
1. Go to https://supermetrics.com/api
2. Sign up for account
3. Enable **Google Ads** connector
4. Create API key in settings
5. Copy the key

**Your API Key looks like**: `aX9mK2pL8qR5vW3xZ7bC`

---

## Step 2: Set Environment Variable

### On Mac/Linux:
```bash
export SUPERMETRICS_API_KEY='your_actual_api_key_here'
echo $SUPERMETRICS_API_KEY  # verify it's set
```

### On Windows (PowerShell):
```powershell
$env:SUPERMETRICS_API_KEY='your_actual_api_key_here'
echo $env:SUPERMETRICS_API_KEY  # verify
```

### Permanent Setup (Optional)
Add to your `.bashrc`, `.zshrc`, or system environment variables to persist.

---

## Step 3: Test the Integration

### Run the Python Script
```bash
cd /home/user/Alluring-Medspa
python3 supermetrics_integration.py
```

### Expected Output
```
============================================================
IVITAMIN GOOGLE ADS DASHBOARD - DATA SUMMARY
============================================================

Period: 2026-05-17 to 2026-06-17

KEY METRICS:
  Revenue:        $48,320.45
  ROAS:           3.82x
  CPA:            $18.50
  Clicks:         2,610
  Conversions:    1,110
  Spend:          $12,850.00
  CTR:            2.84%
  Conv Rate:      4.25%
  CPC:            $4.92

TOP CAMPAIGNS:
  1. Premium Multivitamin - Search
     Revenue: $18,450.00 | ROAS: 4.30x | Conv: 892
  ...
```

If successful, you'll see:
- ✅ Real metrics from your Google Ads account
- ✅ Campaign breakdown
- ✅ `dashboard_data.json` file created

### Troubleshooting
If you get an error:
- **"SUPERMETRICS_API_KEY not set"** → Run export command again
- **"Connection refused"** → Check internet connection
- **"Invalid API key"** → Verify key is correct in Supermetrics dashboard
- **"No data returned"** → Check your Google Ads account has campaigns

---

## Step 4: Update Dashboard to Use Real Data

### Quick Update (Manual)
1. Run the Python script: `python3 supermetrics_integration.py`
2. Open the generated `dashboard_data.json`
3. Copy the metrics into the HTML dashboard (replace sample data)

### Automated Update (Recommended)
See **Step 5** below for automated daily refresh.

---

## Step 5: Set Up Automated Daily Refresh

### Option A: Cron Job (Mac/Linux)

1. **Edit crontab**:
   ```bash
   crontab -e
   ```

2. **Add this line** (runs daily at 10 AM):
   ```bash
   0 10 * * * cd /home/user/Alluring-Medspa && export SUPERMETRICS_API_KEY='your_api_key' && python3 supermetrics_integration.py >> /tmp/dashboard_refresh.log 2>&1
   ```

3. **Verify it's set**:
   ```bash
   crontab -l
   ```

### Option B: Windows Task Scheduler

1. **Create batch file** (`refresh_dashboard.bat`):
   ```batch
   @echo off
   cd C:\path\to\Alluring-Medspa
   set SUPERMETRICS_API_KEY=your_api_key_here
   python supermetrics_integration.py
   ```

2. **Open Task Scheduler**:
   - Press `Win + R` → type `taskscheduler.msc`
   - Click "Create Basic Task"
   - Name: "IVitamin Dashboard Refresh"
   - Trigger: Daily at 10 AM
   - Action: Run program → Select your batch file
   - Click OK

### Option C: GitHub Actions (Cloud-based, recommended)

1. **Create folder structure**:
   ```
   .github/
   └── workflows/
       └── refresh-dashboard.yml
   ```

2. **Create file** `.github/workflows/refresh-dashboard.yml`:
   ```yaml
   name: Daily Dashboard Refresh

   on:
     schedule:
       - cron: '0 10 * * *'  # 10 AM UTC daily
     workflow_dispatch:  # Manual trigger

   jobs:
     refresh:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.9'
         
         - name: Install dependencies
           run: pip install requests
         
         - name: Fetch Supermetrics data
           env:
             SUPERMETRICS_API_KEY: ${{ secrets.SUPERMETRICS_API_KEY }}
           run: python supermetrics_integration.py
         
         - name: Commit and push
           run: |
             git config user.name "Dashboard Bot"
             git config user.email "bot@ivitamin.com"
             git add dashboard_data.json
             git commit -m "Update dashboard data - $(date)" || true
             git push
   ```

3. **Add secret to GitHub**:
   - Go to your repo → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `SUPERMETRICS_API_KEY`
   - Value: Your actual API key
   - Click "Add secret"

4. **Verify it runs**:
   - Go to Actions tab → see "Daily Dashboard Refresh"
   - It runs automatically at 10 AM UTC daily

---

## Step 6: Connect Dashboard to Live Data

### Update HTML Dashboard
Replace the sample data in the dashboard with real data from `dashboard_data.json`:

```javascript
// In the dashboard HTML, add this to fetch real data:
async function loadDashboardData() {
    try {
        const response = await fetch('dashboard_data.json');
        const data = await response.json();
        
        // Update metric cards
        document.querySelector('[data-metric="revenue"]').textContent = 
            '$' + data.metrics.total_revenue.toLocaleString();
        document.querySelector('[data-metric="roas"]').textContent = 
            data.metrics.total_roas + 'x';
        // ... etc for all metrics
    } catch (error) {
        console.error('Error loading dashboard data:', error);
    }
}

// Call on page load
loadDashboardData();
```

---

## Step 7: Monitor Data Freshness

### Check Last Update Time
```bash
ls -la dashboard_data.json
```

### Verify Automation is Working
```bash
# Check last 10 cron job runs (Mac/Linux)
log stream --predicate 'process == "cron"' | head -20
```

---

## What Gets Synced?

### Metrics (Auto-Calculated)
- ✅ Revenue (from conversion values)
- ✅ ROAS (return on ad spend)
- ✅ CPA (cost per acquisition)
- ✅ CTR (click-through rate)
- ✅ Conversion Rate
- ✅ CPC (cost per click)
- ✅ Impressions, Clicks, Conversions

### Data Dimensions
- ✅ Daily trends (for charts)
- ✅ Campaign breakdown
- ✅ Device performance
- ✅ Geographic performance

### Refresh Frequency
- Daily at 10 AM (configurable)
- Last 30 days of data synced
- Automatically overwrites previous data

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No data in `dashboard_data.json` | Check API key is valid; check Google Ads account has data |
| Cron not running | Verify with `crontab -l`; check system permissions |
| Old data still showing | Clear browser cache; hard refresh (Cmd+Shift+R) |
| API rate limiting | Supermetrics allows 100 requests/day on free plan; upgrade if needed |
| Python script errors | Run with `python3 -u` to see full output; check Python 3.7+ installed |

---

## Advanced: Custom Data Fields

### Modify Supermetrics Query
Edit `supermetrics_integration.py` line ~75:

```python
# Add more dimensions
dimensions = ["date", "campaign", "device", "country"]

# Add more metrics
metrics = [
    "impressions", "clicks", "cost", "conversions",
    "conversion_value", "quality_score", "avg_position"
]
```

### Add Custom KPIs
Add to `DashboardDataProcessor.calculate_metrics()`:

```python
# Example: ROAS by quality score
high_quality_revenue = sum(
    float(row.get("conversion_value", 0)) 
    for row in rows if int(row.get("quality_score", 0)) >= 7
)
```

---

## Security Best Practices

⚠️ **NEVER commit your API key to GitHub!**

### Secure your API key:
1. ✅ Store in environment variables
2. ✅ Use GitHub Secrets (for Actions)
3. ✅ Add to `.gitignore`:
   ```
   *.env
   dashboard_data.json
   ```
4. ✅ Rotate API key regularly
5. ✅ Restrict API key permissions in Supermetrics

---

## Performance Tips

- **Dashboard loads slowly?** 
  - Reduce date range: change `days=30` to `days=7`
  - Run refresh less frequently (every 2-3 days)

- **Want real-time updates?**
  - Set cron to run hourly: `0 * * * *`
  - Note: May hit API rate limits

- **Large Google Ads account?**
  - Consider splitting by campaign in the script
  - Query in parallel using Python's `asyncio`

---

## Support

**Need help?**
1. Check logs: `tail -f /tmp/dashboard_refresh.log`
2. Test API key: `curl -H "Authorization: Bearer YOUR_KEY" https://api.supermetrics.com/v1/query`
3. Verify Python: `python3 --version` (must be 3.7+)

---

**Your dashboard is now connected to live Supermetrics data! 🎉**

Next step: Schedule the automation and forget about manual updates.
