"""
Adidas US Sales Data Cleaning Report Generation Script

This script generates a cleaning report from the cleaned dataset.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

# Define file paths
INPUT_FILE = r"c:\Users\Paulo\Documents\Project_Kicks\data\adidas_sales_cleaned.csv"
REPORT_FILE = r"c:\Users\Paulo\Documents\Project_Kicks\data_cleaning\cleaning_report.txt"

def generate_summary_stats(df):
    """Generate summary statistics"""
    report_content = "="*60 + "\n"
    report_content += "DATASET SUMMARY\n"
    report_content += "="*60 + "\n"

    report_content += f"\nTotal Records: {len(df):,}\n"
    report_content += f"Date Range: {df['Invoice Date'].min()} to {df['Invoice Date'].max()}\n"
    report_content += f"\nUnique Values:\n"
    report_content += f"  - Retailers: {df['Retailer'].nunique()}\n"
    report_content += f"  - Regions: {df['Region'].nunique()}\n"
    report_content += f"  - States: {df['State'].nunique()}\n"
    report_content += f"  - Cities: {df['City'].nunique()}\n"
    report_content += f"  - Products: {df['Product'].nunique()}\n"
    report_content += f"  - Sales Methods: {df['Sales Method'].nunique()}\n"

    report_content += f"\nRetailers: {', '.join(df['Retailer'].unique())}\n"
    report_content += f"Regions: {', '.join(df['Region'].unique())}\n"
    report_content += f"Products: {', '.join(df['Product'].unique())}\n"
    report_content += f"Sales Methods: {', '.join(df['Sales Method'].unique())}\n"

    report_content += f"\nFinancial Summary:\n"
    report_content += f"  - Total Sales: ${df['Total Sales'].sum():,.2f}\n"
    report_content += f"  - Total Operating Profit: ${df['Operating Profit'].sum():,.2f}\n"
    report_content += f"  - Average Operating Margin: {df['Operating Margin'].mean():.2%}\n"
    report_content += f"  - Total Units Sold: {df['Units Sold'].sum():,}\n"

    report_content += f"\nPrice Range:\n"
    report_content += f"  - Min: ${df['Price per Unit'].min():.2f}\n"
    report_content += f"  - Max: ${df['Price per Unit'].max():.2f}\n"
    report_content += f"  - Average: ${df['Price per Unit'].mean():.2f}\n"

    return report_content

def save_report(report_content):
    """Save the cleaning report"""
    with open(REPORT_FILE, 'w') as f:
        f.write(report_content)
    print(f"\nCleaning report saved to: {REPORT_FILE}")

def main():
    """Main report generation pipeline"""
    print("="*60)
    print("ADIDAS US SALES REPORT GENERATION PIPELINE")
    print("="*60)

    # Load data
    df = pd.read_csv(INPUT_FILE)
    df['Invoice Date'] = pd.to_datetime(df['Invoice Date'])

    # Generate summary
    report_content = generate_summary_stats(df)

    # Save the report
    save_report(report_content)

    print("\n" + "="*60)
    print("REPORT GENERATION COMPLETED SUCCESSFULLY!")
    print("="*60)

if __name__ == "__main__":
    main()
