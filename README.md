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
### https://github.com/OforiPrescott/Customer-Behavior-and-Sales-Trends.git
### cd sales-dashboard

2. Install Dependencies:
### pip install -r requirements.txt

3. Run the Dashboard:
### streamlit run app.py

### 🔧 Configuration

### Database Connection: Ensure your SQL Server is accessible and update the connection string in app.py:

conn = pyodbc.connect("DRIVER={SQL Server};SERVER=PresHacks;DATABASE=SalesDB;Trusted_Connection=yes")


### Logo Update: Replace logo22.jpg with your company logo in the same directory.
![Screenshot 2025-02-20 151158](https://github.com/user-attachments/assets/4b99f335-c264-4300-a300-134738923acb)

![Screenshot 2025-02-20 151222](https://github.com/user-attachments/assets/0866e5ec-7b4b-420c-88f2-5a7e293eeeb8)
![Screenshot 2025-02-20 151247](https://github.com/user-attachments/assets/e9baaebd-0add-46c1-8e28-cc86cfb7a967)






### 📌 Future Enhancements

### 📊 Regional Sales Breakdown

### 🤖 AI-based Sales Forecasting

### 📍 Geographical Customer Distribution

### 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

### 📜 License

This project is licensed under the MIT License.
