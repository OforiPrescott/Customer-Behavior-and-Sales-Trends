### 📊 Interactive Sales Dashboard ###

This project is an interactive sales dashboard built using Streamlit and Plotly. It connects to a SQL Server database, processes sales data, and provides insightful visualizations for data-driven decision-making.

### 🚀 Features ###

📈 Interactive Charts: Uses Plotly for dynamic visualizations.

🛒 Sales Analysis: Tracks total sales, number of orders, and best-selling products.

📅 Date Filtering: Allows users to filter sales data by date range.

🏆 Top Customers: Identifies high-value customers based on spending.

📦 Product Performance: Shows the distribution of product sales.

📊 Monthly Sales Trends: Displays revenue trends over time.

🔍 Data Exploration: Option to view raw data in a structured table.

### 🏗️ Installation ###
1. Clone the Repository:
### https://github.com/OforiPrescott/Customer-Sales-Trend-.git
### cd sales-dashboard

2. Install Dependencies:
### pip install -r requirements.txt

3. Run the Dashboard:
### streamlit run app.py

### 🔧 Configuration

### Database Connection: Ensure your SQL Server is accessible and update the connection string in app.py:

conn = pyodbc.connect("DRIVER={SQL Server};SERVER=PresHacks;DATABASE=SalesDB;Trusted_Connection=yes")


### Logo Update: Replace logo22.jpg with your company logo in the same directory.

![Screenshot 2025-02-20 151247](https://github.com/user-attachments/assets/3cad636e-7c5f-4b0f-a32b-9b90822f6cc2)

![Screenshot 2025-02-20 151222](https://github.com/user-attachments/assets/a89759f1-8a28-4d81-b0c8-ccb9b64c81cb)

![Screenshot 2025-02-20 151158](https://github.com/user-attachments/assets/73520a7e-d59e-4a83-8d0f-68cd441140f0)





### 📌 Future Enhancements

### 📊 Regional Sales Breakdown

### 🤖 AI-based Sales Forecasting

### 📍 Geographical Customer Distribution

### 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

### 📜 License

This project is licensed under the MIT License.
