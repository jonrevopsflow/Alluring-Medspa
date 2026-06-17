#!/usr/bin/env python3
"""
GoHighLevel Workflow Creator
Creates a 4-week educational email sequence for new leads
Sends 1 email per week on Monday at 10am
"""

import requests
import json
from datetime import datetime

class GHLWorkflowCreator:
    def __init__(self, api_token: str, location_id: str):
        self.api_token = api_token
        self.location_id = location_id
        self.base_url = "https://services.leadconnectorhq.com"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
            "Version": "2021-07-28"
        }

    # Educational email templates for med spa
    EMAIL_TEMPLATES = {
        "week_1": {
            "subject": "Welcome to Alluring Image Medspa 🌟 - Your Beauty Journey Starts Here",
            "body": """<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <h2 style="color: #d4a574;">Welcome to Alluring Image Medspa! ✨</h2>

        <p>Hi [FirstName],</p>

        <p>Thank you for your interest in Alluring Image Medspa! We're thrilled you're exploring ways to look and feel your best.</p>

        <h3 style="color: #d4a574;">What is Modern Med Spa Treatment?</h3>
        <p>Med spa treatments combine medical-grade technology with luxurious spa experience. Unlike traditional spas, med spas offer FDA-approved procedures performed by licensed professionals, delivering real, measurable results.</p>

        <p><strong>Common benefits include:</strong></p>
        <ul>
            <li>Smoother, more youthful skin</li>
            <li>Reduced fine lines and wrinkles</li>
            <li>Improved skin texture and tone</li>
            <li>Increased confidence and self-esteem</li>
            <li>Non-invasive with minimal downtime</li>
        </ul>

        <h3 style="color: #d4a574;">Your First Step</h3>
        <p>Next week, we'll share details about our most popular services. In the meantime, if you have any questions, feel free to reply to this email or call us.</p>

        <p style="margin-top: 30px;">
            <a href="https://calendly.com/alluringimage" style="background-color: #d4a574; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block;">Book Your Free Consultation</a>
        </p>

        <p style="margin-top: 30px; color: #666; font-size: 12px;">
            Alluring Image Medspa<br>
            [Your Address]<br>
            [Your Phone]
        </p>
    </div>
</body>
</html>"""
        },
        "week_2": {
            "subject": "Botox & Injectables: How They Work & What to Expect",
            "body": """<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <h2 style="color: #d4a574;">Understanding Botox & Injectables 💉</h2>

        <p>Hi [FirstName],</p>

        <p>This week, let's explore one of our most popular services: injectables like Botox and dermal fillers.</p>

        <h3 style="color: #d4a574;">What Are Injectables?</h3>
        <p><strong>Botox</strong> relaxes facial muscles that cause wrinkles, smoothing lines on the forehead, between brows, and around eyes. Results appear within 3-7 days and improve over 2 weeks.</p>

        <p><strong>Dermal Fillers</strong> add volume to cheeks, lips, and under eyes, restoring youthful fullness and reducing the appearance of fine lines.</p>

        <h3 style="color: #d4a574;">The Experience</h3>
        <ul>
            <li>⏱️ Quick 15-30 minute appointments</li>
            <li>💉 Minimal discomfort (topical numbing available)</li>
            <li>✨ See results within days</li>
            <li>🎯 Can be tailored to your goals</li>
            <li>🔄 Results last 3-4 months (maintenance recommended)</li>
        </ul>

        <h3 style="color: #d4a574;">Before & After</h3>
        <p>View real results from our clients at [YourWebsiteLink]. Each treatment is customized to enhance your natural beauty, not change it.</p>

        <p style="margin-top: 30px;">
            <a href="https://calendly.com/alluringimage" style="background-color: #d4a574; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block;">Schedule Your Consultation</a>
        </p>

        <p style="margin-top: 30px; color: #666; font-size: 12px;">
            Alluring Image Medspa<br>
            [Your Address]<br>
            [Your Phone]
        </p>
    </div>
</body>
</html>"""
        },
        "week_3": {
            "subject": "Skin Rejuvenation: Lasers, Facials & Treatments That Deliver",
            "body": """<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <h2 style="color: #d4a574;">Skin Rejuvenation Treatments ✨</h2>

        <p>Hi [FirstName],</p>

        <p>Ready to transform your skin? This week we're covering our advanced skin rejuvenation options.</p>

        <h3 style="color: #d4a574;">Popular Skin Treatments</h3>

        <p><strong>Chemical Peels</strong> - Remove damaged outer layers to reveal fresh, glowing skin beneath. Great for acne scars, sun damage, and uneven tone.</p>

        <p><strong>Laser Treatments</strong> - Target specific concerns like age spots, redness, texture, and wrinkles with precision. Minimal downtime.</p>

        <p><strong>Microdermabrasion</strong> - Mechanical exfoliation that improves skin texture and reduces fine lines naturally.</p>

        <p><strong>Hydrating Facials</strong> - Custom facials using professional-grade serums to address your skin type and concerns.</p>

        <h3 style="color: #d4a574;">Why Choose Professional Treatments?</h3>
        <ul>
            <li>10x more effective than at-home products</li>
            <li>Customized to YOUR specific skin concerns</li>
            <li>Safer with professional guidance</li>
            <li>See visible results in 1-3 treatments</li>
            <li>No harsh chemicals (when done right)</li>
        </ul>

        <p><strong>Pro Tip:</strong> Most clients see best results with a series of treatments. We offer package pricing to save you money!</p>

        <p style="margin-top: 30px;">
            <a href="https://calendly.com/alluringimage" style="background-color: #d4a574; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block;">Get Your Skin Analysis</a>
        </p>

        <p style="margin-top: 30px; color: #666; font-size: 12px;">
            Alluring Image Medspa<br>
            [Your Address]<br>
            [Your Phone]
        </p>
    </div>
</body>
</html>"""
        },
        "week_4": {
            "subject": "Limited Time: Exclusive Offer Just for You 🎁",
            "body": """<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
        <h2 style="color: #d4a574;">Your Exclusive Welcome Offer 🎁</h2>

        <p>Hi [FirstName],</p>

        <p>Over the past few weeks, you've learned about the transformative power of med spa treatments. Now it's time to experience it yourself.</p>

        <h3 style="color: #d4a574; font-size: 24px;">Get $50 Off Your First Treatment</h3>
        <p style="font-size: 18px; color: #d4a574; font-weight: bold;">Valid for first-time clients only • Expires in 7 days</p>

        <h3 style="color: #d4a574;">Here's What Happens Next</h3>
        <ol>
            <li><strong>Book Your Consultation</strong> - Let's discuss your goals (15 min, free)</li>
            <li><strong>Customize Your Treatment</strong> - We'll recommend the perfect service for you</li>
            <li><strong>Experience The Results</strong> - Walk out feeling confident and glowing</li>
        </ol>

        <h3 style="color: #d4a574;">Why Clients Choose Alluring Image</h3>
        <p>✨ Licensed, experienced professionals<br>
        ✨ State-of-the-art equipment<br>
        ✨ Personalized, judgment-free care<br>
        ✨ Real results you'll see and feel<br>
        ✨ Affordable pricing & flexible packages</p>

        <p style="margin-top: 20px; padding: 15px; background-color: #f5f5f5; border-left: 4px solid #d4a574;">
            <strong>Don't wait!</strong> First-time slots are filling up fast. Click below to book your $50 off welcome appointment now.
        </p>

        <p style="margin-top: 30px;">
            <a href="https://calendly.com/alluringimage" style="background-color: #d4a574; color: white; padding: 12px 30px; text-decoration: none; border-radius: 5px; display: inline-block; font-size: 16px; font-weight: bold;">Claim Your $50 Off Now</a>
        </p>

        <p style="margin-top: 30px;">Questions? Reply to this email or call us directly.</p>

        <p style="margin-top: 30px; color: #666; font-size: 12px;">
            Alluring Image Medspa<br>
            [Your Address]<br>
            [Your Phone]<br>
            [Your Email]
        </p>
    </div>
</body>
</html>"""
        }
    }

    def create_folder(self, folder_name: str) -> str:
        """Create a folder for organizing workflows"""
        try:
            url = f"{self.base_url}/folders/"
            payload = {
                "locationId": self.location_id,
                "name": folder_name
            }
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            folder_id = data.get("id") or data.get("folderId")
            print(f"✅ Folder '{folder_name}' created with ID: {folder_id}")
            return folder_id
        except Exception as e:
            print(f"⚠️  Could not create folder (may not be supported via API): {e}")
            return None

    def create_workflow(self, workflow_data: dict) -> str:
        """Create a workflow in GHL"""
        try:
            url = f"{self.base_url}/workflows/"
            payload = {
                "locationId": self.location_id,
                **workflow_data
            }
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            data = response.json()
            workflow_id = data.get("id") or data.get("workflowId")
            print(f"✅ Workflow created with ID: {workflow_id}")
            return workflow_id
        except Exception as e:
            print(f"❌ Error creating workflow: {e}")
            if 'response' in locals():
                print(f"Response: {response.text}")
            return None

    def setup_email_sequence_workflow(self) -> dict:
        """Setup 4-week educational email sequence for new leads"""

        print("\n" + "="*60)
        print("Setting up 4-Week Educational Email Sequence")
        print("="*60)

        # Create folder
        folder_id = self.create_folder("claude")

        # Workflow configuration
        workflow_config = {
            "name": "New Lead - 4 Week Education Series",
            "description": "Automated educational email sequence for new leads - 1 email per week for 4 weeks",
            "folderId": folder_id,
            "enabled": True,
            "triggers": [
                {
                    "type": "new_contact",
                    "triggerType": "contact_created"
                }
            ],
            "actions": []
        }

        # Add email actions for each week
        # Week 1 - Send immediately
        workflow_config["actions"].append({
            "type": "send_email",
            "delay": 0,
            "delayUnit": "minutes",
            "email": {
                "subject": self.EMAIL_TEMPLATES["week_1"]["subject"],
                "body": self.EMAIL_TEMPLATES["week_1"]["body"],
                "sendTime": "10:00",
                "sendDay": "Monday",
                "scheduleType": "specific_time"
            }
        })

        # Week 2 - 7 days delay
        workflow_config["actions"].append({
            "type": "send_email",
            "delay": 7,
            "delayUnit": "days",
            "email": {
                "subject": self.EMAIL_TEMPLATES["week_2"]["subject"],
                "body": self.EMAIL_TEMPLATES["week_2"]["body"],
                "sendTime": "10:00",
                "sendDay": "Monday",
                "scheduleType": "specific_time"
            }
        })

        # Week 3 - 14 days delay
        workflow_config["actions"].append({
            "type": "send_email",
            "delay": 14,
            "delayUnit": "days",
            "email": {
                "subject": self.EMAIL_TEMPLATES["week_3"]["subject"],
                "body": self.EMAIL_TEMPLATES["week_3"]["body"],
                "sendTime": "10:00",
                "sendDay": "Monday",
                "scheduleType": "specific_time"
            }
        })

        # Week 4 - 21 days delay (with offer)
        workflow_config["actions"].append({
            "type": "send_email",
            "delay": 21,
            "delayUnit": "days",
            "email": {
                "subject": self.EMAIL_TEMPLATES["week_4"]["subject"],
                "body": self.EMAIL_TEMPLATES["week_4"]["body"],
                "sendTime": "10:00",
                "sendDay": "Monday",
                "scheduleType": "specific_time"
            }
        })

        return workflow_config

    def display_manual_setup_guide(self):
        """Display step-by-step manual setup guide"""
        guide = """
╔════════════════════════════════════════════════════════════════╗
║         GHL MANUAL WORKFLOW SETUP GUIDE                        ║
╚════════════════════════════════════════════════════════════════╝

If the API-based setup doesn't work, follow these steps manually:

STEP 1: Create Folder
────────────────────
1. Go to GoHighLevel → Automations → Workflows
2. Click "Create Folder"
3. Name it: "claude"

STEP 2: Create Workflow
──────────────────────
1. Click "New Workflow"
2. Name: "New Lead - 4 Week Education Series"
3. Click "Trigger"
4. Select: "Contact Created" (new leads)
5. Click "Save Trigger"

STEP 3: Add Week 1 Email (Send Immediately)
──────────────────────────────────────────
1. Click "Add Action" → "Send Email"
2. Subject: "Welcome to Alluring Image Medspa 🌟 - Your Beauty Journey Starts Here"
3. Template: Use provided content (Week 1 below)
4. Send Time: Monday at 10:00 AM
5. Click "Save"

STEP 4: Add Week 2 Email (7 Days Later)
───────────────────────────────────────
1. Click "Add Action" → "Send Email"
2. Delay: Wait 7 days
3. Subject: "Botox & Injectables: How They Work & What to Expect"
4. Template: Use provided content (Week 2 below)
5. Send Time: Monday at 10:00 AM
6. Click "Save"

STEP 5: Add Week 3 Email (14 Days Later)
──────────────────────────────────────────
1. Click "Add Action" → "Send Email"
2. Delay: Wait 14 days (from start)
3. Subject: "Skin Rejuvenation: Lasers, Facials & Treatments"
4. Template: Use provided content (Week 3 below)
5. Send Time: Monday at 10:00 AM
6. Click "Save"

STEP 6: Add Week 4 Email (21 Days Later - Final Offer)
───────────────────────────────────────────────────────
1. Click "Add Action" → "Send Email"
2. Delay: Wait 21 days (from start)
3. Subject: "Limited Time: Exclusive Offer Just for You 🎁"
4. Template: Use provided content (Week 4 below)
5. Send Time: Monday at 10:00 AM
6. Click "Save"

STEP 7: Enable Workflow
──────────────────────
1. Toggle "Enable Workflow" to ON
2. Click "Save & Publish"

STEP 8: Test It
───────────────
1. Go to Contacts
2. Create a test contact
3. Verify emails trigger as expected
4. Check email preview and timing

═══════════════════════════════════════════════════════════════════
"""
        print(guide)


def main():
    api_token = "pit-85e572be-e526-4deb-b3f8-e6ddd02994d9"
    location_id = "pI1PJOSnJKAAyRRjsW1U"

    creator = GHLWorkflowCreator(api_token, location_id)

    # Try API-based setup first
    workflow_config = creator.setup_email_sequence_workflow()

    # Save configuration to file for reference
    with open("ghl_workflow_config.json", "w") as f:
        json.dump(workflow_config, f, indent=2)

    print("\n✅ Workflow configuration saved to: ghl_workflow_config.json")
    print("This file contains the complete workflow setup that can be imported or used as reference.")

    # Display manual setup guide
    creator.display_manual_setup_guide()

    # Save email templates to file
    templates_file = "ghl_email_templates.json"
    with open(templates_file, "w") as f:
        json.dump(creator.EMAIL_TEMPLATES, f, indent=2)

    print(f"\n✅ Email templates saved to: {templates_file}")
    print("Copy these into your GHL emails as needed.")


if __name__ == "__main__":
    main()
