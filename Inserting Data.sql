-- Insert Customers
INSERT INTO Customers (customer_name, email, city, state, country, join_date)
VALUES
('John Doe', 'john@example.com', 'New York', 'NY', 'USA', '2022-01-01'),
('Jane Smith', 'jane@example.com', 'Los Angeles', 'CA', 'USA', '2022-02-15'),
('Alice Johnson', 'alice@example.com', 'Chicago', 'IL', 'USA', '2022-03-10'),
('Bob Brown', 'bob@example.com', 'Houston', 'TX', 'USA', '2022-04-05'),
('Charlie Davis', 'charlie@example.com', 'Phoenix', 'AZ', 'USA', '2022-05-20'),
('Eva Green', 'eva@example.com', 'Philadelphia', 'PA', 'USA', '2022-06-15'),
('Frank Wilson', 'frank@example.com', 'San Antonio', 'TX', 'USA', '2022-07-01'),
('Grace Lee', 'grace@example.com', 'San Diego', 'CA', 'USA', '2022-08-10'),
('Henry Taylor', 'henry@example.com', 'Dallas', 'TX', 'USA', '2022-09-05'),
('Ivy Clark', 'ivy@example.com', 'San Jose', 'CA', 'USA', '2022-10-20');

-- Insert Products
INSERT INTO Products (product_name, category, price, stock_quantity)
VALUES
('Laptop', 'Electronics', 1200.00, 50),
('Smartphone', 'Electronics', 800.00, 100),
('Headphones', 'Accessories', 150.00, 200),
('Tablet', 'Electronics', 600.00, 75),
('Smartwatch', 'Accessories', 250.00, 150),
('Camera', 'Electronics', 900.00, 60),
('Printer', 'Office', 300.00, 80),
('Monitor', 'Electronics', 400.00, 120),
('Keyboard', 'Accessories', 50.00, 300),
('Mouse', 'Accessories', 30.00, 400);

-- Insert Orders
INSERT INTO Orders (customer_id, order_date, total_amount)
VALUES
(1, '2023-01-05', 1200.00),
(2, '2023-02-20', 800.00),
(3, '2023-03-25', 150.00),
(4, '2023-04-10', 600.00),
(5, '2023-05-15', 250.00),
(6, '2023-06-20', 900.00),
(7, '2023-07-25', 300.00),
(8, '2023-08-30', 400.00),
(9, '2023-09-05', 50.00),
(10, '2023-10-10', 30.00);

-- Insert Order Items
INSERT INTO Order_Items (order_id, product_id, quantity, price)
VALUES
(1, 1, 1, 1200.00),
(2, 2, 1, 800.00),
(3, 3, 1, 150.00),
(4, 4, 1, 600.00),
(5, 5, 1, 250.00),
(6, 6, 1, 900.00),
(7, 7, 1, 300.00),
(8, 8, 1, 400.00),
(9, 9, 1, 50.00),
(10, 10, 1, 30.00);
