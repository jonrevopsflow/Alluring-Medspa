# GHL Workflow Setup: 4-Week Educational Email Sequence

## Overview
This workflow automatically sends new leads an educational email sequence over 4 weeks:
- **Week 1**: Welcome + Intro to Med Spa
- **Week 2**: Botox & Injectables Education
- **Week 3**: Skin Rejuvenation Treatments
- **Week 4**: Exclusive $50 Off Offer (Conversion Focus)

**Trigger**: Automatically activates when a new contact/lead is added
**Frequency**: 1 email per week, Mondays at 10:00 AM
**Duration**: 4 weeks

---

## Quick Setup (5 minutes)

### STEP 1: Create Folder "claude"
1. Log into GoHighLevel
2. Go to **Automations → Workflows**
3. Click **"+ New Folder"** (or similar button)
4. Name it: `claude`
5. Click **Save**

### STEP 2: Create New Workflow
1. Inside the "claude" folder, click **"+ New Workflow"**
2. Name: `New Lead - 4 Week Education Series`
3. Description (optional): `Automated educational email sequence for new leads`
4. Click **Create**

### STEP 3: Set Trigger
1. Click **"Add Trigger"**
2. Select: **"Contact Created"** (or "New Contact")
3. Click **Save Trigger**

### STEP 4: Add 4 Email Actions

#### EMAIL 1 - Week 1 (Send Immediately)
1. Click **"+ Add Action"** → **"Send Email"**
2. **Delay**: 0 minutes (send immediately on trigger)
3. **Subject**: `Welcome to Alluring Image Medspa 🌟 - Your Beauty Journey Starts Here`
4. **Body**: Copy from `ghl_email_templates.json` → `week_1` → `body`
5. **Schedule**: Set to send on **Monday at 10:00 AM**
6. Click **Save**

#### EMAIL 2 - Week 2 (7 Days Later)
1. Click **"+ Add Action"** → **"Send Email"**
2. **Delay**: 7 days
3. **Subject**: `Botox & Injectables: How They Work & What to Expect`
4. **Body**: Copy from `ghl_email_templates.json` → `week_2` → `body`
5. **Schedule**: Set to send on **Monday at 10:00 AM**
6. Click **Save**

#### EMAIL 3 - Week 3 (14 Days Later)
1. Click **"+ Add Action"** → **"Send Email"**
2. **Delay**: 14 days (from workflow start)
3. **Subject**: `Skin Rejuvenation: Lasers, Facials & Treatments That Deliver`
4. **Body**: Copy from `ghl_email_templates.json` → `week_3` → `body`
5. **Schedule**: Set to send on **Monday at 10:00 AM**
6. Click **Save**

#### EMAIL 4 - Week 4 (21 Days Later - CONVERSION FOCUS)
1. Click **"+ Add Action"** → **"Send Email"**
2. **Delay**: 21 days (from workflow start)
3. **Subject**: `Limited Time: Exclusive Offer Just for You 🎁`
4. **Body**: Copy from `ghl_email_templates.json` → `week_4` → `body`
5. **Schedule**: Set to send on **Monday at 10:00 AM**
6. Click **Save**

### STEP 5: Enable Workflow
1. Look for **"Enable Workflow"** or **"Activate"** toggle
2. Toggle it **ON**
3. Click **"Save & Publish"**

✅ **Your workflow is now live!**

---

## Email Content Quick Reference

### Week 1: Welcome Email
- **Focus**: Education about med spa
- **Goal**: Build trust and excitement
- **CTA**: Book free consultation
- **Tone**: Welcoming, professional, positive

### Week 2: Botox & Injectables
- **Focus**: Educational content about popular service
- **Goal**: Overcome objections, explain benefits
- **CTA**: Schedule consultation
- **Tone**: Informative, reassuring

### Week 3: Skin Rejuvenation
- **Focus**: Showcase treatment variety
- **Goal**: Show options beyond injectables
- **CTA**: Get skin analysis
- **Tone**: Educational, empowering

### Week 4: Exclusive Offer
- **Focus**: Limited-time conversion offer ($50 off)
- **Goal**: Drive immediate action
- **CTA**: Claim offer now
- **Tone**: Urgent but friendly

---

## Important Notes

### Customization
Before publishing, make sure to update these placeholders in each email:
- `[FirstName]` - GHL will auto-fill with contact's first name
- `[Your Address]` - Your medspa location
- `[Your Phone]` - Your phone number
- `[Your Email]` - Your business email
- `https://calendly.com/alluringimage` - Replace with your booking link
- `[YourWebsiteLink]` - Link to your before/after gallery

### Scheduling
- All emails set for **Monday at 10:00 AM** for consistency
- GHL will respect the contact's timezone if configured
- You can adjust time if needed (e.g., Tuesday 9:00 AM)

### Testing
Before going live:
1. Add yourself as a test contact
2. Verify emails arrive at correct times
3. Check formatting and personalization
4. Click all links to ensure they work
5. Review subject lines for spam filters

### Monitoring
Once live:
1. Track **Email Open Rate** (target: 30%+)
2. Track **Click-Through Rate** (target: 5-10%)
3. Track **Conversion Rate** (appointments booked)
4. Monitor **Unsubscribe Rate** (should be <0.5%)

---

## Expected Results

Based on med spa industry benchmarks:

| Week | Expected Opens | Expected Clicks | Expected Bookings |
|------|----------------|-----------------|-------------------|
| 1    | 30-40%         | 3-5%            | 5-8%              |
| 2    | 25-35%         | 3-5%            | 3-5%              |
| 3    | 20-30%         | 3-5%            | 3-5%              |
| 4    | 35-50%         | 8-12%           | 10-15%            |

**Total Expected Conversion**: 15-25% of new leads → customers

---

## Troubleshooting

### Emails not sending?
- Check that workflow is **enabled**
- Verify trigger is set to **"Contact Created"**
- Ensure contact has an email address
- Check GHL's email deliverability status

### Wrong timing?
- Verify delay settings (0, 7, 14, 21 days)
- Check contact's timezone settings
- Test with your own email first

### Need to modify emails?
- Go to Workflow → Click email action
- Click "Edit Email"
- Make changes
- Save and publish

### Want to add more actions?
- Add SMS follow-ups before/after emails
- Add SMS appointments reminders (48 & 24 hours before)
- Add post-appointment review requests
- Add Win-back campaigns for non-converters

---

## Next Steps

1. ✅ **Set up this workflow** (follow steps above)
2. ✅ **Test with yourself** (add as test contact)
3. ✅ **Monitor performance** (track opens, clicks, conversions)
4. ✅ **Optimize based on data** (A/B test subject lines)
5. ✅ **Scale by adding more workflows** (SMS sequence, post-appointment, etc.)

---

## Files Provided

- **ghl_email_templates.json** - Complete email content (copy/paste ready)
- **ghl_workflow_config.json** - Workflow configuration (reference)
- **ghl_workflow_creator.py** - Python script that created this
- **GHL_WORKFLOW_SETUP.md** - This file

---

## Questions?

If you need to adjust:
- **Email timing**: Change delays (0, 7, 14, 21)
- **Day of week**: Change from Monday to any other day
- **Send time**: Change from 10:00 AM to preferred time
- **Content**: Edit emails in the templates file
- **Offer**: Change $50 off to whatever promotion you want

Let me know what adjustments you need!
