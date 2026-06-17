# GHL Workflow Setup - Manual (Step by Step)

## Location of Everything in GHL

### Where to Find Workflows
1. **Log into GoHighLevel** → https://app.gohighlevel.com/
2. Go to **Left Sidebar → Automations**
3. Click **"Workflows"** (or "Funnels & Automations")
4. You'll see a list of existing workflows

---

## STEP 1: Create the Folder "claude" 
*(Optional but recommended for organization)*

1. In **Automations → Workflows** section
2. Look for **"+ New Folder"** button (usually top right)
3. Click it
4. Type: `claude`
5. Click **Create** or **Save**

---

## STEP 2: Create New Workflow

1. In the workflows area, click **"+ New Workflow"** or **"Create Workflow"**
2. Fill in:
   - **Name**: `New Lead - 4 Week Education Series`
   - **Description** (optional): `Sends new leads educational emails for 4 weeks`
3. Click **Create**

You should now be in the workflow builder (blank canvas).

---

## STEP 3: Add the Trigger (When to Start)

Look for a button that says **"Add Trigger"** or **"+ Add"** at the top of the workflow canvas.

1. Click **"Add Trigger"**
2. Select: **"Contact Created"** or **"New Contact"**
   - This means: "Start this workflow whenever a new lead is added"
3. Click **Save Trigger**

---

## STEP 4: Add Email #1 (Week 1 - Welcome Email)

### Add the Action
1. Look for **"+ Add Action"** button on the workflow canvas
2. Click it
3. Select **"Send Email"**

### Configure Email #1
Fill in these fields:

| Field | Value |
|-------|-------|
| **Email** | Select an existing email or create new |
| **Subject** | `Welcome to Alluring Image Medspa 🌟 - Your Beauty Journey Starts Here` |
| **Send Delay** | 0 minutes (send right away) |
| **Scheduled Time** | Monday at 10:00 AM |

### Email Body (Copy & Paste)
Go to your `ghl_email_templates.json` file and copy the **week_1 → body** content.

Paste it into the email body field in GHL.

**Before publishing, replace these in the email:**
- `[FirstName]` → Leave as is (GHL will auto-fill)
- `[Your Address]` → Your medspa address
- `[Your Phone]` → Your phone number
- `https://calendly.com/alluringimage` → Your booking link

Click **Save**

---

## STEP 5: Add Email #2 (Week 2 - Botox & Injectables)

1. Click **"+ Add Action"** again
2. Select **"Send Email"**

Fill in:

| Field | Value |
|-------|-------|
| **Subject** | `Botox & Injectables: How They Work & What to Expect` |
| **Send Delay** | 7 days |
| **Scheduled Time** | Monday at 10:00 AM |

Copy **week_2 → body** from `ghl_email_templates.json` into the body.

Update placeholders like before.

Click **Save**

---

## STEP 6: Add Email #3 (Week 3 - Skin Rejuvenation)

1. Click **"+ Add Action"** again
2. Select **"Send Email"**

Fill in:

| Field | Value |
|-------|-------|
| **Subject** | `Skin Rejuvenation: Lasers, Facials & Treatments That Deliver` |
| **Send Delay** | 14 days |
| **Scheduled Time** | Monday at 10:00 AM |

Copy **week_3 → body** from `ghl_email_templates.json` into the body.

Update placeholders.

Click **Save**

---

## STEP 7: Add Email #4 (Week 4 - Offer Email)

1. Click **"+ Add Action"** again
2. Select **"Send Email"**

Fill in:

| Field | Value |
|-------|-------|
| **Subject** | `Limited Time: Exclusive Offer Just for You 🎁` |
| **Send Delay** | 21 days |
| **Scheduled Time** | Monday at 10:00 AM |

Copy **week_4 → body** from `ghl_email_templates.json` into the body.

Update placeholders.

Click **Save**

---

## STEP 8: Enable & Publish Workflow

1. Look for an **"Enable Workflow"** toggle or button (usually top right)
2. Toggle it **ON** (should turn green)
3. Click **"Save & Publish"** or **"Save"**

✅ **Your workflow is now LIVE!**

---

## TEST IT (Very Important!)

1. Go to **Contacts**
2. Click **"+ Add Contact"** or **"New Contact"**
3. Add a test contact (use your email address)
4. Make sure it's marked as **new contact** (not lead or existing)
5. Wait for emails to arrive

Expected: You should receive an email almost immediately (Week 1 email), then one each week after.

---

## Quick Reference: What Goes Where

### Email 1 (Day 0 - Immediately)
```
Subject: Welcome to Alluring Image Medspa 🌟 - Your Beauty Journey Starts Here
Delay: 0 minutes
Body: Copy from ghl_email_templates.json → week_1 → body
```

### Email 2 (Day 7)
```
Subject: Botox & Injectables: How They Work & What to Expect
Delay: 7 days
Body: Copy from ghl_email_templates.json → week_2 → body
```

### Email 3 (Day 14)
```
Subject: Skin Rejuvenation: Lasers, Facials & Treatments That Deliver
Delay: 14 days
Body: Copy from ghl_email_templates.json → week_3 → body
```

### Email 4 (Day 21)
```
Subject: Limited Time: Exclusive Offer Just for You 🎁
Delay: 21 days
Body: Copy from ghl_email_templates.json → week_4 → body
```

---

## Common Issues

### Can't find "Add Trigger"?
- Make sure you're in the workflow builder (canvas view)
- Look at top of the canvas
- Should say something like "Untouched" or show trigger area

### Can't find "Add Action"?
- Click on the trigger box first
- A connector line should appear
- Click **"+ Add Action"** below the trigger

### Email body looks weird?
- You're likely in code view
- Switch to **"HTML"** or **"Visual"** editor
- Paste content into the right view

### Emails arriving in spam?
- Check subject line (too many emojis can trigger spam filters)
- Verify sender email is authenticated in GHL
- Test with multiple email addresses

### Want to test without going live?
- Create workflow with trigger set to **"Manual Only"** first
- Test by manually triggering it
- Then change trigger to **"Contact Created"** when ready

---

## Need Help?

If you get stuck:
1. Take a screenshot of where you're stuck
2. Describe what you see
3. Let me know the exact field or button name you're looking for

I can help you troubleshoot!
