# Sales Data Analysis Pipeline

A comprehensive end-to-end data analysis project that demonstrates the complete workflow from raw data ingestion to business insights using Python, Pandas, SQLite, and data visualization.

## 🎯 Project Overview

This project implements a complete sales data analysis pipeline that includes:

- Data generation and exploration
- Data cleaning and validation
- Database storage and management
- SQL-based business analysis
- Data visualization and insights

## 📁 Project Structure

```
sales_analysis/
├── sample_sales_data.csv          # Generated sample dataset
├── sales.db                       # SQLite database
├── sales_analytics_pipeline.py    # Main analysis script
└── README.md                      # Project documentation
```

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **SQLite3** - Database management
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualizations

## 📊 Dataset Features

The project uses a realistic sample sales dataset containing:

- **2,500+ transaction records**
- **Date range**: 2023-2024
- **6 product categories**: Electronics, Clothing, Home & Garden, Sports, Books, Toys
- **5 geographical regions**: North, South, East, West, Central
- **10 sales representatives**
- **Intentional data quality issues** for cleaning practice

### Dataset Columns:

- `order_id` - Unique transaction identifier
- `order_date` - Transaction date
- `customer_id` - Customer identifier
- `product_name` - Product purchased
- `category` - Product category
- `quantity` - Items purchased
- `unit_price` - Price per item
- `region` - Sales region
- `sales_rep` - Sales representative
- `total_sales` - Total transaction value
- `order_type` - Sale or Refund classification

## 🔧 Data Quality Issues Addressed

The project demonstrates handling of common real-world data problems:

- ✅ **Missing values** (3% of records)
- ✅ **Duplicate records** (3 duplicates)
- ✅ **Inconsistent formatting** (case sensitivity, extra spaces)
- ✅ **Invalid dates** (10 impossible date entries)
- ✅ **Negative quantities** (5 data entry errors)
- ✅ **Price outliers** (8 unrealistic values)
- ✅ **Calculation errors** (floating-point precision issues)

## 📋 Analysis Workflow

### 1. Data Exploration

- Dataset structure assessment
- Data type validation
- Missing value identification
- Unique value analysis for categorical fields
- Numeric field validation

### 2. Data Cleaning

- Duplicate removal
- Text standardization (strip whitespace, title case)
- Missing value imputation with business-logical defaults
- Date format correction
- Negative quantity handling
- Calculation validation and correction

### 3. Database Integration

- SQLite database creation
- Table schema design
- Data loading and verification
- Connection management

### 4. SQL Business Analysis

#### Basic Analysis:

- Monthly/quarterly sales trends
- Best-selling products by quantity
- Regional performance comparison
- Top-performing sales representatives

#### Intermediate Analysis:

- Average order value by category
- Customer purchase frequency analysis
- Seasonal sales patterns
- Sales vs. refunds breakdown

#### Advanced Analysis:

- Sales performance trending over time
- Customer lifetime value by region
- Statistical distribution analysis

## 📈 Key Business Insights

The analysis provides insights into:

- **Sales Trends**: Monthly performance patterns
- **Product Performance**: Top-selling items and categories
- **Geographic Analysis**: Regional sales distribution
- **Team Performance**: Sales rep effectiveness
- **Customer Behavior**: Purchase patterns and lifetime value
- **Business Health**: Sales vs. refunds ratio

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas sqlite3 matplotlib seaborn
```

### Running the Analysis

1. Clone or download the project files
2. Ensure all required libraries are installed
3. Run the main script:

```bash
python sales_analytics_pipeline.py
```

### Expected Outputs

- Data quality assessment reports
- Cleaned dataset statistics
- SQL query results for all business questions
- Visualization charts for trend analysis
- SQLite database with cleaned data

## 📊 Sample Queries

### Monthly Sales Trend

```sql
SELECT strftime('%Y-%m', order_date) AS year_month,
       SUM(total_sales) as monthly_sales
FROM sales_data
GROUP BY year_month
ORDER BY year_month
```

### Top Products by Quantity

```sql
SELECT product_name,
       SUM(quantity) AS total_quantity_sold
FROM sales_data
GROUP BY product_name
ORDER BY total_quantity_sold DESC
```

### Regional Performance

```sql
SELECT region,
       strftime('%Y', order_date) as year,
       SUM(total_sales) as regional_sales
FROM sales_data
GROUP BY region, year
ORDER BY year
```

## 📈 Visualizations

The project includes several data visualizations:

- **Line charts** for sales trends over time
- **Box plots** for customer lifetime value distribution
- **Statistical summaries** for performance metrics

## 🎓 Learning Outcomes

This project demonstrates proficiency in:

- **Data Engineering**: ETL processes, data cleaning, validation
- **Database Management**: SQLite integration, schema design
- **SQL Analytics**: Complex queries, aggregations, business analysis
- **Data Visualization**: Trend analysis, statistical plotting
- **Python Programming**: Pandas operations, data manipulation
- **Business Intelligence**: KPI calculation, performance metrics

## 🔍 Future Enhancements

Potential extensions for this project:

- Integration with real-world data sources (APIs, web scraping)
- Advanced analytics (cohort analysis, RFM segmentation)
- Interactive dashboards (Plotly, Streamlit)
- Machine learning models (sales forecasting, customer segmentation)
- Automated reporting and scheduling

## 📝 Notes

- The dataset contains intentionally introduced data quality issues for educational purposes
- All business questions follow standard retail analytics practices
- SQL queries are optimized for learning and can be adapted for larger datasets
- Database connection remains open throughout the analysis for query efficiency

## 🤝 Contributing

This project serves as a learning template. Feel free to:

- Extend the analysis with additional business questions
- Implement more advanced data cleaning techniques
- Add new visualization types
- Integrate additional data sources

---

**Project Type**: Educational Data Analysis Pipeline  
**Complexity Level**: Intermediate  
**Estimated Completion Time**: 4-6 hours  
**Skills Demonstrated**: Python, Pandas, SQL, Data Visualization, Business Analysis
