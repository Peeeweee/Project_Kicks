from flask import render_template, current_app, jsonify
from . import bp
import plotly.express as px
import plotly.graph_objects as go
import json

@bp.route('/customer')
def index():
    """Customer Patterns page"""
    df = current_app.df
    
    # Calculate KPIs
    total_sales = df['Total Sales'].sum()
    total_profit = df['Operating Profit'].sum()
    total_units = df['Units Sold'].sum()
    avg_margin = df['Operating Margin'].mean()
    total_transactions = len(df)

    start_date = df['Invoice Date'].min().strftime('%B %d, %Y')
    end_date = df['Invoice Date'].max().strftime('%B %d, %Y')

    num_retailers = df['Retailer'].nunique()
    num_regions = df['Region'].nunique()
    num_products = df['Product'].nunique()

    kpis = {
        'total_sales': f'${total_sales:,.0f}',
        'total_profit': f'${total_profit:,.0f}',
        'total_units': f'{total_units:,}',
        'avg_margin': f'{avg_margin:.1%}',
        'total_transactions': f'{total_transactions:,}',
        'start_date': start_date,
        'end_date': end_date,
        'num_retailers': num_retailers,
        'num_regions': num_regions,
        'num_products': num_products,
    }

    return render_template('index.html', kpis=kpis, active_tab='customer-patterns')
