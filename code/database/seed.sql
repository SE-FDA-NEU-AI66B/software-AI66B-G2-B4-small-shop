USE mini_shop;


-- 1 CUSTOMER_TYPES
INSERT INTO customer_types (type_name, discount_percent)
VALUES
('Walk-in', 0.00),
('Silver', 5.00),
('Gold', 10.00),
('Diamond', 15.00);

-- 2 CATEGORIES
INSERT INTO categories (category_name)
VALUES
('Coffee'),
('Tea'),
('Milk Tea'),
('Pastry'),
('Food'),
('Dessert');

-- 3 EMPLOYEES
INSERT INTO employees (name, phone, email, role, status, created_at)
VALUES
('Nguyen Ha Vy', '0901234567', 'havy@yums.com', 'Manager', 'Active', '2026-01-10'),
('Tran Minh Anh', '0912345678', 'minhanh@yums.com', 'Employee', 'Active', '2026-01-10'),
('Le Quang Huy', '0923456789', 'quanghuy@yums.com', 'Employee', 'Active', '2026-01-10'),
('Pham Thu Trang', '0934567890', 'thutrang@yums.com', 'Employee', 'Active', '2026-01-10'),
('Do Duc Anh', '0945678901', 'ducanh@yums.com', 'Employee', 'Inactive', '2026-01-10');

-- 4 CUSTOMERS 
INSERT INTO customers
(name, phone, email, total_spent, customer_type_id)
VALUES
('Nguyen Van An', '0981000001', 'an@gmail.com', 1250000, 3),
('Tran Thu Ha', '0981000002', 'ha@gmail.com', 680000, 2),
('Le Minh Duc', '0981000003', 'duc@gmail.com', 2500000, 4),
('Pham Ngoc Mai', '0981000004', 'mai@gmail.com', 320000, 2),
('Hoang Gia Bao', '0981000005', 'bao@gmail.com', 95000, 1),
('Vu Thanh Hoa', '0981000006', 'hoa@gmail.com', 1850000, 3),
('Do Minh Quan', '0981000007', 'quan@gmail.com', 150000, 1),
('Bui Khanh Linh', '0981000008', 'linh@gmail.com', 4200000, 4);

-- 5 PRODUCTS
INSERT INTO products
(name, category_id, unit_price)
VALUES
('Espresso', 1, 35000),
('Americano', 1, 40000),
('Cappuccino', 1, 45000),
('Latte', 1, 45000),

('Green Tea', 2, 30000),
('Peach Tea', 2, 40000),
('Lemon Tea', 2, 35000),

('Classic Milk Tea', 3, 45000),
('Brown Sugar Milk Tea', 3, 50000),
('Matcha Milk Tea', 3, 50000),

('Croissant', 4, 35000),
('Chocolate Muffin', 4, 40000),
('Butter Cookie', 4, 25000),

('Chicken Sandwich', 5, 55000),
('Beef Sandwich', 5, 65000),

('Cheesecake', 6, 55000),
('Tiramisu', 6, 60000),
('Ice Cream', 6, 40000);

-- 6 INVENTORY
INSERT INTO inventory (product_id, quantity, stocked_at)
VALUES 
(1, 50, '2026-10-01'), -- available
(2, 40, '2026-09-30'),

(3, 3, '2026-10-01'), -- low_stock
(4, 5, '2026-09-25'), -- expiry

(5, 20, '2026-09-27'), -- near
(6, 10, '2026-09-26');

-- 7 ORDERS
INSERT INTO `orders` (`employee_id`, `customer_id`) 
VALUES 
(1, 1),
(2, 2),
(3, 5);

-- 8 ORDER ITEMS
INSERT INTO `order_items` (`order_id`, `product_id`, `quantity`) 
VALUES 
(1, 1, 2),
(1, 2, 1),
(2, 3, 1),
(3, 18, 20),
(3, 16, 15),
(3, 1, 15);

UPDATE `orders` SET `deliver_status` = 'delivered' WHERE `order_id` = 3;

INSERT INTO `orders` (`employee_id`, `customer_id`, `deliver_status`) 
VALUES 
(1, 4, 'delivered');
INSERT INTO `order_items` (`order_id`, `product_id`, `quantity`) 
VALUES 
(6, 1, 1);

SELECT * FROM inventory;
SELECT * FROM products;
SELECT * FROM orders;
SELECT * FROM order_items;
SELECT * FROM customers;