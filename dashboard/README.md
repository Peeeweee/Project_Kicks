# Kicks: Adidas US Sales Dashboard

A comprehensive Flask-based web dashboard for visualizing and analyzing Adidas US Sales data.

## Features

### Key Performance Indicators (KPIs)
- **Total Sales**: Gross revenue generated across all transactions
- **Operating Profit**: Total profit earned
- **Units Sold**: Total number of products sold
- **Average Margin**: Average profit margin across all sales

### Interactive Visualizations

1. **Sales Trend Over Time**: Monthly sales performance showing growth patterns and seasonality
2. **Sales by Region**: Geographic distribution across 5 US regions
3. **Product Category Performance**: Sales distribution across 6 product categories (footwear and apparel)
4. **Retailer Performance**: Comparison across 6 retail partners
5. **Sales Channel**: Performance breakdown by In-store, Outlet, and Online channels
6. **Top Performing States**: Top 10 states by total sales revenue
7. **Operating Margin Analysis**: Profitability comparison across product categories
8. **Quarterly Performance**: Sales and profit trends by quarter
9. **Price Distribution**: Distribution of product prices across all sales

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly (interactive charts)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Montserrat)

## Installation

1. Navigate to the dashboard directory:
   ```bash
   cd dashboard
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Dashboard

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. The dashboard will automatically load all visualizations

## Project Structure

```
dashboard/
├── app.py                  # Main Flask application with routes and API endpoints
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/
│   └── index.html         # Main dashboard HTML template
└── static/
    ├── css/
    │   └── style.css      # Custom CSS styling
    ├── js/                # JavaScript files (if needed)
    └── images/            # Dashboard images/assets
```

## API Endpoints

- `/` - Main dashboard page
- `/api/sales-trend` - Monthly sales trend data
- `/api/sales-by-region` - Sales by region data
- `/api/product-performance` - Product category performance
- `/api/retailer-performance` - Retailer performance data
- `/api/sales-method` - Sales by channel data
- `/api/top-states` - Top 10 states by sales
- `/api/margin-analysis` - Operating margin by product
- `/api/quarterly-performance` - Quarterly sales and profit
- `/api/price-distribution` - Price distribution histogram
- `/api/summary-stats` - Summary statistics (JSON)

## Data Source

The dashboard uses the cleaned Adidas US Sales dataset located at:
```
../data/adidas_sales_cleaned.csv
```

Dataset includes:
- **9,648** transactions
- **2 years** of sales data (2020-2021)
- **6 retailers**: Foot Locker, Walmart, Sports Direct, West Gear, Kohl's, Amazon
- **5 regions**: Northeast, South, West, Midwest, Southeast
- **50 states** across the US
- **6 product categories**: Men's/Women's Street Footwear, Athletic Footwear, and Apparel

## Customization

### Color Scheme
The dashboard uses Adidas brand colors defined in `static/css/style.css`:
- Primary (Black): #000000
- Secondary (Blue): #0057B8
- Success (Green): #00A651
- Warning (Yellow): #FDB913
- Danger (Red): #E4002B

### Adding New Visualizations
1. Create a new API endpoint in `app.py`
2. Add a new chart container in `templates/index.html`
3. Update the JavaScript to load the new chart

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Opera

## Performance

- All charts load asynchronously for optimal performance
- Responsive design adapts to all screen sizes
- Interactive charts with hover tooltips and zoom capabilities

## License

This dashboard is part of the Project_Kicks analytics suite.

## Author

Created for comprehensive Adidas US Sales analysis and business intelligence.