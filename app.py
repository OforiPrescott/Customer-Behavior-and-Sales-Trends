import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")

# Add the uploaded logo
st.sidebar.image("logo22.jpg", use_column_width=True)

# Database connection function
@st.cache_data
def load_data():
    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=PresHacks;DATABASE=SalesDB;Trusted_Connection=yes")
    customers_df = pd.read_sql("SELECT * FROM Customers", conn)
    orders_df = pd.read_sql("SELECT * FROM Orders", conn)
    products_df = pd.read_sql("SELECT * FROM Products", conn)
    order_items_df = pd.read_sql("SELECT * FROM Order_Items", conn)
    conn.close()
    return customers_df, orders_df, products_df, order_items_df

customers_df, orders_df, products_df, order_items_df = load_data()

# Merge data for analysis
merged_df = (
    orders_df
    .merge(customers_df, on="customer_id")
    .merge(order_items_df, on="order_id")
    .merge(products_df, on="product_id")
)

# Convert order_date to datetime
merged_df["order_date"] = pd.to_datetime(merged_df["order_date"])

# Sidebar Filters
st.sidebar.header("Filters")

min_date, max_date = merged_df["order_date"].min(), merged_df["order_date"].max()
start_date = st.sidebar.date_input("Start Date", min_date)
end_date = st.sidebar.date_input("End Date", max_date)

selected_customer = st.sidebar.multiselect("Select Customer(s)", options=merged_df["customer_name"].unique(), default=merged_df["customer_name"].unique())
selected_product = st.sidebar.multiselect("Select Product(s)", options=merged_df["product_name"].unique(), default=merged_df["product_name"].unique())

# Apply filters
filtered_df = merged_df[
    (merged_df["order_date"] >= pd.to_datetime(start_date)) &
    (merged_df["order_date"] <= pd.to_datetime(end_date)) &
    (merged_df["customer_name"].isin(selected_customer)) &
    (merged_df["product_name"].isin(selected_product))
]

# Key Metrics
st.subheader("📊 Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sales", f"GH₵{filtered_df['total_amount'].sum():,.2f}")
with col2:
    st.metric("Number of Orders", filtered_df['order_id'].nunique())
with col3:
    top_product = filtered_df["product_name"].mode()[0] if not filtered_df.empty else "N/A"
    st.metric("Top Product", top_product)

# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")
filtered_df["month"] = filtered_df["order_date"].dt.to_period("M")
monthly_sales = filtered_df.groupby("month")["total_amount"].sum().reset_index()
monthly_sales["month"] = monthly_sales["month"].astype(str)
fig = px.line(monthly_sales, x="month", y="total_amount", markers=True, title="Sales Over Time", labels={"month": "Month", "total_amount": "Total Sales"})
st.plotly_chart(fig, use_container_width=True)

# Top Customers
st.subheader("🏆 Top 5 Customers by Spending")
top_customers = filtered_df.groupby("customer_name")["total_amount"].sum().nlargest(5).reset_index()
fig = px.bar(top_customers, x="customer_name", y="total_amount", title="Top Customers", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

# Product Sales Breakdown
st.subheader("📦 Product Sales Breakdown")
product_sales = filtered_df.groupby("product_name")["quantity"].sum().reset_index()
fig = px.pie(product_sales, names="product_name", values="quantity", title="Product Sales Share")
st.plotly_chart(fig, use_container_width=True)

# Raw Data
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)
