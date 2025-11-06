"""
Adidas US Sales Data Cleaning Script

This script cleans and prepares the Adidas US Sales dataset for analysis by:
1. Removing header rows and empty columns
2. Converting data types (dates, numeric values)
3. Removing formatting ($ signs, commas, %)
4. Handling missing values
5. Validating data quality
6. Exporting cleaned dataset
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

# Define file paths
INPUT_FILE = r"c:\Users\Paulo\Documents\Project_Kicks\data\Adidas US Sales Datasets - Data Sales Adidas.csv"
OUTPUT_FILE = r"c:\Users\Paulo\Documents\Project_Kicks\data\adidas_sales_cleaned.csv"
REPORT_FILE = r"c:\Users\Paulo\Documents\Project_Kicks\data_cleaning\cleaning_report.txt"

def load_raw_data():
    """Load the raw data, skipping header rows"""
    print("Loading raw data...")
    # Skip the first 4 rows (empty headers), use row 5 as column names
    df = pd.read_csv(INPUT_FILE, skiprows=4)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    return df

def remove_empty_columns(df):
    """Remove columns that are completely empty or unnamed"""
    print("\nRemoving empty columns...")
    # Get columns that start with 'Unnamed'
    unnamed_cols = [col for col in df.columns if str(col).startswith('Unnamed')]
    if unnamed_cols:
        df = df.drop(columns=unnamed_cols)
        print(f"Removed {len(unnamed_cols)} unnamed/empty columns")
    return df

def clean_currency_columns(df):
    """Remove $ signs and commas from currency columns"""
    print("\nCleaning currency columns...")
    currency_columns = ['Price per Unit', 'Total Sales', 'Operating Profit']

    for col in currency_columns:
        if col in df.columns:
            # Remove $ and commas, then convert to float
            df[col] = df[col].astype(str).str.replace('$', '', regex=False)
            df[col] = df[col].str.replace(',', '', regex=False)
            df[col] = pd.to_numeric(df[col], errors='coerce')
            print(f"  - Cleaned {col}")

    return df

def clean_numeric_columns(df):
    """Clean numeric columns (Units Sold)"""
    print("\nCleaning numeric columns...")

    if 'Units Sold' in df.columns:
        # Remove commas and convert to integer
        df['Units Sold'] = df['Units Sold'].astype(str).str.replace(',', '', regex=False)
        df['Units Sold'] = pd.to_numeric(df['Units Sold'], errors='coerce')
        df['Units Sold'] = df['Units Sold'].astype('Int64')  # Use nullable integer type
        print("  - Cleaned Units Sold")

    return df

def clean_percentage_columns(df):
    """Clean percentage columns"""
    print("\nCleaning percentage columns...")

    if 'Operating Margin' in df.columns:
        # Remove % sign and convert to decimal
        df['Operating Margin'] = df['Operating Margin'].astype(str).str.replace('%', '', regex=False)
        df['Operating Margin'] = pd.to_numeric(df['Operating Margin'], errors='coerce')
        # Convert from percentage to decimal (e.g., 50% -> 0.50)
        df['Operating Margin'] = df['Operating Margin'] / 100
        print("  - Cleaned Operating Margin (converted to decimal)")

    return df

def clean_date_columns(df):
    """Convert date columns to datetime"""
    print("\nCleaning date columns...")

    if 'Invoice Date' in df.columns:
        df['Invoice Date'] = pd.to_datetime(df['Invoice Date'], errors='coerce')
        print("  - Converted Invoice Date to datetime")

        # Add additional date-based columns for analysis
        df['Year'] = df['Invoice Date'].dt.year
        df['Month'] = df['Invoice Date'].dt.month
        df['Month_Name'] = df['Invoice Date'].dt.month_name()
        df['Quarter'] = df['Invoice Date'].dt.quarter
        df['Day_of_Week'] = df['Invoice Date'].dt.day_name()
        print("  - Added Year, Month, Month_Name, Quarter, Day_of_Week columns")

    return df

def clean_text_columns(df):
    """Clean and standardize text columns"""
    print("\nCleaning text columns...")

    text_columns = ['Retailer', 'Region', 'State', 'City', 'Product', 'Sales Method']

    for col in text_columns:
        if col in df.columns:
            # Strip whitespace and standardize
            df[col] = df[col].astype(str).str.strip()
            # Remove any leading/trailing whitespace
            df[col] = df[col].replace('nan', np.nan)

    print(f"  - Cleaned {len(text_columns)} text columns")
    return df

def validate_data(df):
    """Validate data quality and identify issues"""
    print("\n" + "="*60)
    print("DATA VALIDATION REPORT")
    print("="*60)

    issues = []

    # Check for missing values
    print("\nMissing Values:")
    missing = df.isnull().sum()
    if missing.any():
        for col, count in missing[missing > 0].items():
            pct = (count / len(df)) * 100
            print(f"  - {col}: {count} ({pct:.2f}%)")
            issues.append(f"Missing values in {col}: {count} ({pct:.2f}%)")
    else:
        print("  No missing values found!")

    # Check for negative values in numeric columns
    print("\nNegative Values Check:")
    numeric_cols = ['Price per Unit', 'Units Sold', 'Total Sales', 'Operating Profit']
    has_negatives = False
    for col in numeric_cols:
        if col in df.columns:
            negatives = (df[col] < 0).sum()
            if negatives > 0:
                print(f"  - {col}: {negatives} negative values")
                issues.append(f"Negative values in {col}: {negatives}")
                has_negatives = True
    if not has_negatives:
        print("  No negative values found!")

    # Check for duplicate rows
    print("\nDuplicate Rows Check:")
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"  Found {duplicates} duplicate rows")
        issues.append(f"Duplicate rows: {duplicates}")
    else:
        print("  No duplicate rows found!")

    # Data consistency checks
    print("\nData Consistency Checks:")
    # Check if Total Sales = Price per Unit * Units Sold
    df['Calculated_Total_Sales'] = df['Price per Unit'] * df['Units Sold']
    sales_mismatch = (abs(df['Total Sales'] - df['Calculated_Total_Sales']) > 0.01).sum()
    if sales_mismatch > 0:
        print(f"  - Total Sales calculation mismatch: {sales_mismatch} rows")
        issues.append(f"Total Sales calculation mismatch: {sales_mismatch} rows")
    else:
        print("  - Total Sales calculations are consistent!")

    # Drop the temporary column
    df = df.drop(columns=['Calculated_Total_Sales'])

    # Check if Operating Profit = Total Sales * Operating Margin
    df['Calculated_Operating_Profit'] = df['Total Sales'] * df['Operating Margin']
    profit_mismatch = (abs(df['Operating Profit'] - df['Calculated_Operating_Profit']) > 0.01).sum()
    if profit_mismatch > 0:
        print(f"  - Operating Profit calculation mismatch: {profit_mismatch} rows")
        issues.append(f"Operating Profit calculation mismatch: {profit_mismatch} rows")
    else:
        print("  - Operating Profit calculations are consistent!")

    # Drop the temporary column
    df = df.drop(columns=['Calculated_Operating_Profit'])

    return df, issues

def generate_summary_stats(df):
    """Generate summary statistics"""
    print("\n" + "="*60)
    print("DATASET SUMMARY")
    print("="*60)

    print(f"\nTotal Records: {len(df):,}")
    print(f"Date Range: {df['Invoice Date'].min()} to {df['Invoice Date'].max()}")
    print(f"\nUnique Values:")
    print(f"  - Retailers: {df['Retailer'].nunique()}")
    print(f"  - Regions: {df['Region'].nunique()}")
    print(f"  - States: {df['State'].nunique()}")
    print(f"  - Cities: {df['City'].nunique()}")
    print(f"  - Products: {df['Product'].nunique()}")
    print(f"  - Sales Methods: {df['Sales Method'].nunique()}")

    print(f"\nRetailers: {', '.join(df['Retailer'].unique())}")
    print(f"Regions: {', '.join(df['Region'].unique())}")
    print(f"Products: {', '.join(df['Product'].unique())}")
    print(f"Sales Methods: {', '.join(df['Sales Method'].unique())}")

    print(f"\nFinancial Summary:")
    print(f"  - Total Sales: ${df['Total Sales'].sum():,.2f}")
    print(f"  - Total Operating Profit: ${df['Operating Profit'].sum():,.2f}")
    print(f"  - Average Operating Margin: {df['Operating Margin'].mean():.2%}")
    print(f"  - Total Units Sold: {df['Units Sold'].sum():,}")

    print(f"\nPrice Range:")
    print(f"  - Min: ${df['Price per Unit'].min():.2f}")
    print(f"  - Max: ${df['Price per Unit'].max():.2f}")
    print(f"  - Average: ${df['Price per Unit'].mean():.2f}")

def save_cleaned_data(df):
    """Save the cleaned dataset"""
    print(f"\nSaving cleaned data to: {OUTPUT_FILE}")
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Cleaned dataset saved successfully!")
    print(f"File size: {os.path.getsize(OUTPUT_FILE) / (1024*1024):.2f} MB")

def save_report(report_content):
    """Save the cleaning report"""
    with open(REPORT_FILE, 'w') as f:
        f.write(report_content)
    print(f"\nCleaning report saved to: {REPORT_FILE}")

def main():
    """Main cleaning pipeline"""
    print("="*60)
    print("ADIDAS US SALES DATA CLEANING PIPELINE")
    print("="*60)

    # Load data
    df = load_raw_data()

    # Display initial info
    print(f"\nInitial columns: {list(df.columns)}")

    # Clean data
    df = remove_empty_columns(df)
    df = clean_currency_columns(df)
    df = clean_numeric_columns(df)
    df = clean_percentage_columns(df)
    df = clean_date_columns(df)
    df = clean_text_columns(df)

    # Validate data
    df, issues = validate_data(df)

    # Generate summary
    generate_summary_stats(df)

    # Display final column info
    print("\n" + "="*60)
    print("CLEANED DATASET STRUCTURE")
    print("="*60)
    print(f"\nFinal columns ({len(df.columns)}):")
    for i, col in enumerate(df.columns, 1):
        dtype = df[col].dtype
        print(f"  {i}. {col} ({dtype})")

    # Save cleaned data
    save_cleaned_data(df)

    print("\n" + "="*60)
    print("DATA CLEANING COMPLETED SUCCESSFULLY!")
    print("="*60)

    return df

if __name__ == "__main__":
    cleaned_df = main()