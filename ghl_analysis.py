#!/usr/bin/env python3
"""
GoHighLevel API analysis tool for Alluring Image Medspa
Fetches leads, opportunities, emails, and SMS data
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any

class GHLAnalyzer:
    def __init__(self, api_token: str, location_id: str):
        self.api_token = api_token
        self.location_id = location_id
        self.base_url = "https://api.gohighlevel.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    def get_leads(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Fetch all leads for the location"""
        try:
            url = f"{self.base_url}/contacts"
            params = {
                "locationId": self.location_id,
                "limit": limit
            }
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("contacts", [])
        except Exception as e:
            print(f"Error fetching leads: {e}")
            return []

    def get_opportunities(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Fetch all opportunities for the location"""
        try:
            url = f"{self.base_url}/opportunities"
            params = {
                "locationId": self.location_id,
                "limit": limit
            }
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("opportunities", [])
        except Exception as e:
            print(f"Error fetching opportunities: {e}")
            return []

    def get_emails(self) -> List[Dict[str, Any]]:
        """Fetch email communication logs"""
        try:
            url = f"{self.base_url}/conversations/email"
            params = {
                "locationId": self.location_id,
                "limit": 100
            }
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("emails", [])
        except Exception as e:
            print(f"Error fetching emails: {e}")
            return []

    def get_sms(self) -> List[Dict[str, Any]]:
        """Fetch SMS communication logs"""
        try:
            url = f"{self.base_url}/conversations/sms"
            params = {
                "locationId": self.location_id,
                "limit": 100
            }
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("sms", [])
        except Exception as e:
            print(f"Error fetching SMS: {e}")
            return []

    def analyze_account(self) -> Dict[str, Any]:
        """Run complete account analysis"""
        print("🔍 Fetching GoHighLevel account data...")

        leads = self.get_leads()
        opportunities = self.get_opportunities()
        emails = self.get_emails()
        sms = self.get_sms()

        # Calculate metrics
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "location_id": self.location_id,
            "summary": {
                "total_leads": len(leads),
                "total_opportunities": len(opportunities),
                "total_emails": len(emails),
                "total_sms": len(sms),
            },
            "lead_analysis": self._analyze_leads(leads),
            "opportunity_analysis": self._analyze_opportunities(opportunities),
            "communication_analysis": {
                "email_count": len(emails),
                "sms_count": len(sms),
                "total_communications": len(emails) + len(sms)
            },
            "raw_data": {
                "leads": leads,
                "opportunities": opportunities,
                "emails": emails,
                "sms": sms
            }
        }

        return analysis

    def _analyze_leads(self, leads: List[Dict]) -> Dict[str, Any]:
        """Analyze lead data"""
        if not leads:
            return {"total": 0, "status_breakdown": {}, "sources": []}

        status_breakdown = {}
        sources = {}

        for lead in leads:
            status = lead.get("status", "unknown")
            source = lead.get("source", "unknown")

            status_breakdown[status] = status_breakdown.get(status, 0) + 1
            sources[source] = sources.get(source, 0) + 1

        return {
            "total": len(leads),
            "status_breakdown": status_breakdown,
            "sources": sources
        }

    def _analyze_opportunities(self, opportunities: List[Dict]) -> Dict[str, Any]:
        """Analyze opportunity data"""
        if not opportunities:
            return {"total": 0, "status_breakdown": {}, "total_value": 0}

        status_breakdown = {}
        total_value = 0

        for opp in opportunities:
            status = opp.get("status", "unknown")
            value = float(opp.get("value", 0) or 0)

            status_breakdown[status] = status_breakdown.get(status, 0) + 1
            total_value += value

        return {
            "total": len(opportunities),
            "status_breakdown": status_breakdown,
            "total_value": total_value,
            "avg_value": total_value / len(opportunities) if opportunities else 0
        }


def main():
    # Configuration
    api_token = "pit-85e572be-e526-4deb-b3f8-e6ddd02994d9"
    location_id = "pI1PJOSnJKAAyRRjsW1U"

    analyzer = GHLAnalyzer(api_token, location_id)
    analysis = analyzer.analyze_account()

    # Save results
    with open("/home/user/Alluring-Medspa/ghl_analysis_results.json", "w") as f:
        json.dump(analysis, f, indent=2)

    # Print summary
    print("\n" + "="*60)
    print("ALLURING IMAGE MEDSPA - GHL ACCOUNT ANALYSIS")
    print("="*60)
    print(f"\n📊 SUMMARY:")
    print(f"  Total Leads: {analysis['summary']['total_leads']}")
    print(f"  Total Opportunities: {analysis['summary']['total_opportunities']}")
    print(f"  Total Emails: {analysis['summary']['total_emails']}")
    print(f"  Total SMS: {analysis['summary']['total_sms']}")

    if analysis['lead_analysis']['total'] > 0:
        print(f"\n👥 LEAD ANALYSIS:")
        print(f"  Total Leads: {analysis['lead_analysis']['total']}")
        print(f"  Status Breakdown: {analysis['lead_analysis']['status_breakdown']}")
        print(f"  Sources: {analysis['lead_analysis']['sources']}")

    if analysis['opportunity_analysis']['total'] > 0:
        print(f"\n💰 OPPORTUNITY ANALYSIS:")
        print(f"  Total Opportunities: {analysis['opportunity_analysis']['total']}")
        print(f"  Status Breakdown: {analysis['opportunity_analysis']['status_breakdown']}")
        print(f"  Total Value: ${analysis['opportunity_analysis']['total_value']:,.2f}")
        print(f"  Avg Value: ${analysis['opportunity_analysis']['avg_value']:,.2f}")

    print(f"\n📧 COMMUNICATION:")
    print(f"  Emails: {analysis['communication_analysis']['email_count']}")
    print(f"  SMS: {analysis['communication_analysis']['sms_count']}")
    print(f"  Total: {analysis['communication_analysis']['total_communications']}")

    print(f"\n✅ Full analysis saved to: ghl_analysis_results.json")
    print("="*60)


if __name__ == "__main__":
    main()
