#!/usr/bin/env python3
"""
Supermetrics API Integration for IVitamin Google Ads Dashboard
Fetches real-time Google Ads data from Supermetrics API
"""

import requests
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SupermetricsConnector:
    """Connect to Supermetrics API and fetch Google Ads data"""

    def __init__(self, api_key: str):
        """
        Initialize Supermetrics connector

        Args:
            api_key: Your Supermetrics API key
        """
        self.api_key = api_key
        self.base_url = "https://api.supermetrics.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def query_google_ads(
        self,
        date_from: str = None,
        date_to: str = None,
        dimensions: List[str] = None,
        metrics: List[str] = None
    ) -> Dict[str, Any]:
        """
        Query Google Ads data from Supermetrics

        Args:
            date_from: Start date (YYYY-MM-DD)
            date_to: End date (YYYY-MM-DD)
            dimensions: Dimensions to group by (campaign, date, device, etc.)
            metrics: Metrics to fetch (impressions, clicks, cost, conversions, etc.)

        Returns:
            Dictionary with query results
        """

        if not date_from:
            date_from = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        if not date_to:
            date_to = datetime.now().strftime("%Y-%m-%d")

        if not dimensions:
            dimensions = ["date", "campaign"]
        if not metrics:
            metrics = ["impressions", "clicks", "cost", "conversions"]

        payload = {
            "datasource": "googleppc",  # Google Ads data source
            "date_from": date_from,
            "date_to": date_to,
            "dimensions": dimensions,
            "metrics": metrics
        }

        try:
            logger.info(f"Querying Google Ads data from {date_from} to {date_to}")
            response = requests.post(
                f"{self.base_url}/query",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            logger.info(f"Successfully fetched {len(data.get('rows', []))} rows")
            return data
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Supermetrics: {e}")
            return {"error": str(e), "rows": []}

    def get_campaign_performance(self) -> Dict[str, Any]:
        """
        Get campaign-level performance data
        """
        return self.query_google_ads(
            dimensions=["campaign", "date"],
            metrics=[
                "impressions",
                "clicks",
                "cost",
                "conversions",
                "conversion_value"
            ]
        )

    def get_daily_metrics(self, days: int = 30) -> Dict[str, Any]:
        """
        Get daily aggregate metrics for trend analysis
        """
        date_from = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        return self.query_google_ads(
            date_from=date_from,
            dimensions=["date"],
            metrics=[
                "impressions",
                "clicks",
                "cost",
                "conversions",
                "conversion_value"
            ]
        )

    def get_device_performance(self) -> Dict[str, Any]:
        """
        Get device-level performance (mobile, desktop, tablet)
        """
        return self.query_google_ads(
            dimensions=["device", "campaign"],
            metrics=[
                "impressions",
                "clicks",
                "cost",
                "conversions",
                "conversion_value"
            ]
        )

    def get_geographic_performance(self) -> Dict[str, Any]:
        """
        Get geographic performance data
        """
        return self.query_google_ads(
            dimensions=["country", "region", "city"],
            metrics=[
                "impressions",
                "clicks",
                "cost",
                "conversions",
                "conversion_value"
            ]
        )


class DashboardDataProcessor:
    """Process Supermetrics data for dashboard consumption"""

    @staticmethod
    def calculate_metrics(data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate dashboard KPIs from raw Supermetrics data
        """
        rows = data.get("rows", [])

        if not rows:
            return {
                "total_revenue": 0,
                "total_roas": 0,
                "total_cpa": 0,
                "total_clicks": 0,
                "total_impressions": 0,
                "total_conversions": 0,
                "total_spend": 0,
                "ctr": 0,
                "conversion_rate": 0,
                "cpc": 0
            }

        total_spend = sum(float(row.get("cost", 0)) for row in rows)
        total_conversions = sum(int(row.get("conversions", 0)) for row in rows)
        total_revenue = sum(float(row.get("conversion_value", 0)) for row in rows)
        total_clicks = sum(int(row.get("clicks", 0)) for row in rows)
        total_impressions = sum(int(row.get("impressions", 0)) for row in rows)

        # Calculate KPIs
        roas = total_revenue / total_spend if total_spend > 0 else 0
        cpa = total_spend / total_conversions if total_conversions > 0 else 0
        ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
        conversion_rate = (total_conversions / total_clicks * 100) if total_clicks > 0 else 0
        cpc = total_spend / total_clicks if total_clicks > 0 else 0

        return {
            "total_revenue": round(total_revenue, 2),
            "total_roas": round(roas, 2),
            "total_cpa": round(cpa, 2),
            "total_clicks": total_clicks,
            "total_impressions": total_impressions,
            "total_conversions": total_conversions,
            "total_spend": round(total_spend, 2),
            "ctr": round(ctr, 2),
            "conversion_rate": round(conversion_rate, 2),
            "cpc": round(cpc, 2)
        }

    @staticmethod
    def format_campaign_data(data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Format campaign data for dashboard table
        """
        rows = data.get("rows", [])
        campaign_data = {}

        for row in rows:
            campaign = row.get("campaign", "Unknown")

            if campaign not in campaign_data:
                campaign_data[campaign] = {
                    "campaign": campaign,
                    "impressions": 0,
                    "clicks": 0,
                    "spend": 0,
                    "conversions": 0,
                    "revenue": 0
                }

            campaign_data[campaign]["impressions"] += int(row.get("impressions", 0))
            campaign_data[campaign]["clicks"] += int(row.get("clicks", 0))
            campaign_data[campaign]["spend"] += float(row.get("cost", 0))
            campaign_data[campaign]["conversions"] += int(row.get("conversions", 0))
            campaign_data[campaign]["revenue"] += float(row.get("conversion_value", 0))

        # Calculate KPIs per campaign
        for campaign in campaign_data.values():
            campaign["roas"] = (
                campaign["revenue"] / campaign["spend"]
                if campaign["spend"] > 0 else 0
            )
            campaign["cpa"] = (
                campaign["spend"] / campaign["conversions"]
                if campaign["conversions"] > 0 else 0
            )
            campaign["cpc"] = (
                campaign["spend"] / campaign["clicks"]
                if campaign["clicks"] > 0 else 0
            )
            campaign["ctr"] = (
                (campaign["clicks"] / campaign["impressions"] * 100)
                if campaign["impressions"] > 0 else 0
            )
            campaign["conversion_rate"] = (
                (campaign["conversions"] / campaign["clicks"] * 100)
                if campaign["clicks"] > 0 else 0
            )

            # Round for display
            campaign["spend"] = round(campaign["spend"], 2)
            campaign["revenue"] = round(campaign["revenue"], 2)
            campaign["roas"] = round(campaign["roas"], 2)
            campaign["cpa"] = round(campaign["cpa"], 2)
            campaign["cpc"] = round(campaign["cpc"], 2)
            campaign["ctr"] = round(campaign["ctr"], 2)
            campaign["conversion_rate"] = round(campaign["conversion_rate"], 2)

        return sorted(campaign_data.values(), key=lambda x: x["revenue"], reverse=True)

    @staticmethod
    def format_daily_trend(data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Format daily data for trend charts
        """
        rows = data.get("rows", [])
        return [
            {
                "date": row.get("date"),
                "revenue": float(row.get("conversion_value", 0)),
                "clicks": int(row.get("clicks", 0)),
                "conversions": int(row.get("conversions", 0)),
                "spend": float(row.get("cost", 0))
            }
            for row in sorted(rows, key=lambda x: x.get("date", ""))
        ]


class DashboardAPI:
    """REST API for dashboard data"""

    def __init__(self, api_key: str, avg_order_value: float = 100):
        """
        Initialize Dashboard API

        Args:
            api_key: Supermetrics API key
            avg_order_value: Average value per conversion (for revenue calculation)
        """
        self.connector = SupermetricsConnector(api_key)
        self.processor = DashboardDataProcessor()
        self.aov = avg_order_value

    def get_dashboard_data(self) -> Dict[str, Any]:
        """
        Get all data needed for dashboard
        """
        logger.info("Fetching dashboard data...")

        # Fetch data from Supermetrics
        daily_data = self.connector.get_daily_metrics(days=30)
        campaign_data = self.connector.get_campaign_performance()

        # Process data
        metrics = self.processor.calculate_metrics(daily_data)
        campaigns = self.processor.format_campaign_data(campaign_data)
        trends = self.processor.format_daily_trend(daily_data)

        dashboard_data = {
            "timestamp": datetime.now().isoformat(),
            "metrics": metrics,
            "campaigns": campaigns,
            "trends": trends,
            "period": {
                "start": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                "end": datetime.now().strftime("%Y-%m-%d")
            }
        }

        logger.info("Dashboard data prepared successfully")
        return dashboard_data

    def save_to_json(self, filename: str = "dashboard_data.json"):
        """
        Save dashboard data to JSON file
        """
        data = self.get_dashboard_data()
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        logger.info(f"Dashboard data saved to {filename}")
        return filename


def main():
    """
    Main execution
    """
    # Get API key from environment variable
    api_key = os.getenv("SUPERMETRICS_API_KEY")

    if not api_key:
        print("Error: SUPERMETRICS_API_KEY environment variable not set")
        print("\nTo use this script:")
        print("1. Get your Supermetrics API key from https://supermetrics.com/api")
        print("2. Set environment variable: export SUPERMETRICS_API_KEY='your_key_here'")
        print("3. Run this script")
        return

    # Initialize and fetch data
    api = DashboardAPI(api_key)
    data = api.get_dashboard_data()

    # Print summary
    print("\n" + "="*60)
    print("IVITAMIN GOOGLE ADS DASHBOARD - DATA SUMMARY")
    print("="*60)
    print(f"\nPeriod: {data['period']['start']} to {data['period']['end']}")
    print(f"\nKEY METRICS:")
    print(f"  Revenue:        ${data['metrics']['total_revenue']:,.2f}")
    print(f"  ROAS:           {data['metrics']['total_roas']:.2f}x")
    print(f"  CPA:            ${data['metrics']['total_cpa']:.2f}")
    print(f"  Clicks:         {data['metrics']['total_clicks']:,}")
    print(f"  Conversions:    {data['metrics']['total_conversions']:,}")
    print(f"  Spend:          ${data['metrics']['total_spend']:,.2f}")
    print(f"  CTR:            {data['metrics']['ctr']:.2f}%")
    print(f"  Conv Rate:      {data['metrics']['conversion_rate']:.2f}%")
    print(f"  CPC:            ${data['metrics']['cpc']:.2f}")

    print(f"\nTOP CAMPAIGNS:")
    for i, campaign in enumerate(data['campaigns'][:5], 1):
        print(f"  {i}. {campaign['campaign']}")
        print(f"     Revenue: ${campaign['revenue']:,.2f} | ROAS: {campaign['roas']:.2f}x | Conv: {campaign['conversions']}")

    print(f"\nDashboard data points: {len(data['trends'])} days")
    print("="*60)

    # Save to file
    api.save_to_json()


if __name__ == "__main__":
    main()
