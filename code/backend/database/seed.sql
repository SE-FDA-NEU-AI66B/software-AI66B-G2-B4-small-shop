USE mini_shop;


-- 1 CUSTOMER_TYPES
INSERT INTO customer_types (type_name, discount_percent)
VALUES
('Rock', 0.00),
('Bronze', 5.00),
('Silver', 15.00),
('Gold', 30.00);

-- 2 CATEGORIES
INSERT INTO categories (category_name)
VALUES
('Coffee'),
('Tea'),
('Milk Tea'),
('Pastry'),
('Food'),
('Dessert');

-- 3 USER
INSERT INTO users(username, password, role)
VALUES
('havy', '$2b$12$GnRbPRHYkKdx.wTmol84f.zb205mUaGNWSvu50ZO0Y7MVu4gW.0lO', 'Admin'), -- 12345
('minhanh', '$2b$12$5m7wkDaLLs9oH2ymLxRHp.Gw1rL7TVOnNM3V3D1lGS0zmWw.rxcSG', 'Employee'), -- minhanh
('quanghuy', '$2b$12$Ys.i/f99eRkkji8Rs.bg/.xM6A.La4rSWRGpowlnZcIOEtDGw/vwS', 'Employee'), -- quanghuy
('thutrang', '$2b$12$wd79ID6ttO/eb0yt/vI0lO8dZlAIaw0eAUTwuKsSt38hvhSumYh.a', 'Employee'),
('ducanh', '$2b$12$QWelM1jh2v9qdLZalHn7du.ZermdBxMa3F42nbNGd/ZsevvRIqTz6', 'Employee'),	
('an_nv', 'mã_hoá', 'Manager'),
('binh_tt', 'mã_hoá', 'Employee'),
('cuong_lv', 'mã_hoá', 'Employee'),
('dung_pt', 'mã_hoá', 'Employee'),
('em_hv', 'mã_hoá', 'Employee'),
('hoa_vt', 'mã_hoá', 'Employee'),
('hung_dv', 'mã_hoá', 'Employee'),
('lan_bt', 'mã_hoá', 'Employee'),
('minh_dv', 'mã_hoá', 'Employee'),
('nga_nt', 'mã_hoá', 'Manager'),
('long_pv', 'mã_hoá', 'Employee'),
('mai_ht', 'mã_hoá', 'Employee'),
('nam_vq', 'mã_hoá', 'Employee'),
('phuong_dt', 'mã_hoá', 'Employee'),
('son_bv', 'mã_hoá', 'Employee');

-- 4 EMPLOYEES
INSERT INTO employees (name, username, phone, role, status)
VALUES
('Nguyen Ha Vy', 'havy', '0901234567', 'Manager', 'Active'),
('Tran Minh Anh', 'minhanh', '0912345678', 'Staff', 'Active'),
('Le Quang Huy', 'quanghuy', '0923456789', 'Staff', 'On Leave'),
('Pham Thu Trang', 'thutrang', '0934567890', 'Staff', 'Active'),
('Do Duc Anh', 'ducanh', '0945678901', 'Staff', 'Inactive'),
('Nguyen Van An', 'an_nv', '0901234567', 'Manager', 'Active'),
('Tran Thi Binh', 'binh_tt', '0912345678', 'Staff', 'Active'),
('Le Van Cuong', 'cuong_lv', '0923456789', 'Cashier', 'On Leave'),
('Pham Thi Dung', 'dung_pt', '0934567890', 'Staff', 'Active'),
('Hoang Van Em', 'em_hv', '0945678901', 'Cashier', 'Active'),
('Vu Thi Hoa', 'hoa_vt', '0956789012', 'Staff', 'Inactive'),
('Dang Van Hung', 'hung_dv', '0967890123', 'Cashier', 'Active'),
('Bui Thi Lan', 'lan_bt', '0978901234', 'Staff', 'On Leave'),
('Do Van Minh', 'minh_dv', '0989012345', 'Cashier', 'Inactive'),
('Nguyen Thi Nga', 'nga_nt', '0990123456', 'Manager', 'On Leave'),
('Pham Van Long', 'long_pv', '0903234567', 'Cashier', 'Active'),
('Hoang Thi Mai', 'mai_ht', '0914345678', 'Staff', 'Active'),
('Vu Quoc Nam', 'nam_vq', '0925456789', 'Cashier', 'On Leave'),
('Dang Thi Phuong', 'phuong_dt', '0936567890', 'Staff', 'Inactive'),
('Bui Van Son', 'son_bv', '0947678901', 'Cashier', 'On Leave');

-- 5 CUSTOMERS 
INSERT INTO customers
(name, phone, total_spent, customer_type_id)
VALUES
('Nguyen Van An', '0981000001', 1250000, 4), 
('Tran Thu Ha', '0981000002', 680000, 3),    
('Le Minh Duc', '0981000003', 2500000, 4), 
('Pham Ngoc Mai', '0981000004', 320000, 2), 
('Hoang Gia Bao', '0981000005', 95000, 1),  
('Vu Thanh Hoa', '0981000006', 1850000, 4), 
('Do Minh Quan', '0981000007', 150000, 2), 
('Bui Khanh Linh', '0981000008', 4200000, 4);

-- 6 PRODUCTS
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

-- 7 INVENTORY
INSERT INTO inventory (product_id, quantity)
VALUES 
(1, 50), 
(2, 40),

(3, 3), 
(4, 5), 

(5, 20), 
(6, 10);

-- 8 ORDERS
INSERT INTO orders (employee_id, customer_id, note)
VALUES
    (1, 1, 'Customer requested extra sweet.'),
    (2, 2, 'Please use non-lactose milk.'),
    (3, 5, 'Customer prefers cool-served.'),
    (4, 3, NULL);

-- 9 ORDER ITEMS
INSERT INTO order_items (`order_id`, `product_id`, `quantity`)
VALUES 
(1, 1, 4),
(2, 2, 1),
(2, 10, 4),
(3, 5, 2),
(4, 11, 1);

