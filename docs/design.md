# Milestone 2 - Walking skeleton
## Architecture

## Data model
![](https://github.com/SE-FDA-NEU-AI66B/software-AI66B-G2-B4-small-shop/blob/66_design_data_model/docs/images/erd.png)
| Table              | Columns                                                                                                                         | Constraint · which M1 rule                                                                                                                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **employees**      | `employee_id` PK · `name` · `phone` · `email` · `role` · `status` · `created_at`                                                | `employee_id` uniquely identifies each employee · `role` and `status` are required · supports employee management · **US14**                                                                                                    |
| **customer_types** | `customer_type_id` PK · `type_name` · `discount_percent`                                                                        | `customer_type_id` uniquely identifies each customer type · `discount_percent` defaults to 0 · supports membership discounts · **BR6**                                                                                          |
| **customers**      | `customer_id` PK · `name` · `phone` · `email` · `total_spent` · `customer_type_id` FK · `created_at`                            | `customer_type_id` links a customer to their customer type · `total_spent` stores accumulated spending · supports customer management and membership assignment · **US12, US13, BR6**                                           |
| **categories**     | `category_id` PK · `category_name`                                                                                              | `category_id` uniquely identifies each product category · products are grouped by category · **US08**                                                                                                                           |
| **products**       | `product_id` PK · `name` · `category_id` FK · `unit_price` · `is_available` BOOL                                                | `category_id` references `categories` · `is_available` prevents unavailable products from being added to orders · **BR1**                                                                                                       |
| **inventory**      | `inventory_id` PK · `product_id` FK · `quantity` · `stocked_at` · `expiry_date` · `status`                                      | `product_id` references `products` · expired products are marked `Expired` and excluded from sale · products close to expiry are marked `Near Expiration` · low quantity is marked `Low Stock` · **BR4, BR5**                   |
| **orders**         | `order_id` PK · `employee_id` FK · `customer_id` FK NULL · `deliver_status` · `total_amount` · `discount_amount` · `created_at` | `employee_id` references the employee creating the order · `customer_id` may be NULL for walk-in customers · `total_amount` and `discount_amount` are calculated from order items and customer type · **US01, US02, US06, BR6** |
| **order_items**    | `order_item_id` PK · `order_id` FK · `product_id` FK · `quantity` · `unit_price` · `subtotal`                                   | `order_id` and `product_id` reference their parent records · unavailable products cannot be added · `subtotal` is calculated from `quantity × unit_price` · **BR1**                                                             |



## API design

## Walking skeleton

## Design Decisions
### ADR01: Web application (with responsive) instead of phone only or desktop only application
**Options:**
- Desktop-only application
- Mobile-only application
- Responsive application

**Chose:** Responsive application    
**Why:** Because the current trend in small business’s demands on management platforms is portability and convenience, thus a web platform that they can open anywhere, anytime, on any device - a cashier counter’s desktop, an employee or manager’s personal phone they’re carrying around… without complicated installation.    
**What would change our mind:** If the customers demand specific software functions such as document scanning using camera, or frequent push notifications pushing, we would consider leaning on mobile application more.    

### ADR02: MySQL instead of SQLite or PostgreSQL
**Options:**
- MySQL
- SQLite
- PostgreSQL

**Chose:** MySQL    
**Why:** In this project, we need to record orders, products/inventory list, customers, employees, and sale records in a relational database. SQLite, despite being lightweight and simple to set up, isn’t too friendly to having multiple users accessing at once, while F&B businesses are more likely to have at least several workers during the same shift. On the other hand, PostgreSQL is advanced yet more complicated than what’s enough for us. Therefore MySQL is the best choice for us since it’s relatively simple yet still provides all required relational database features.    
**What would change our mind:** If the customers require more advanced analytical queries or higher scalability, we would consider switching to PostgreSQL; or SQLite if simplicity became the top priority and the system was used by only one worker at once.    

### ADR03: Automatic membership tier assignment instead of manual assignment
**Options:**
- Manual assignment
- Automatic assignment

**Chose:** Automatic assignment.    
**Why:** As our membership tier rule is based on how much a registered customer spent and they’ll upgrade their tier once they reach a certain amount of spending, automatic assignment based on total spending can save us effort and time in assigning it manually, as well as avoid making mistakes when the number of customers increases.    
**What would change our mind:** If the shop’s membership tier assignment mechanism wasn’t based solely on total spending but on other mechanisms, we would decide another calculating mechanism or allow the managers to assign this manually.    

### ADR04: In-app low-stock and expired alerts instead of via email/SMS
**Options:**
- In-app notifications
- Email notifications
- SMS notifications

**Chose: In-app notifications**    
**Why:** This function is for managers only, who open the app very frequently, so direct in-app notification is much simpler and won’t involve third party costs (which Email or SMS may require).    
**What would change our mind:** If the managers feel it’s very urgent to see notifications even when they’re not opening the app so they wouldn’t miss anything, we would consider a still-relatively simple yet regular and easy to access like SMS.    

### ADR05: Manager’s functions covering Employee’s functions instead of two different sets of function
**Options:**
- Employee and Manager having distinct functions without mingling
- Manager’s functions covering all Employee’s function

**Chose: Manager’s functions covering all Employee’s function**    
**Why:** This gives managers authority to perform Employee’s function when the shop is short-staffed (not the other way around because Manager is at a higher role hierarchy than Employee). This also reduces maintenance and development efforts.    
**What would change our mind:** If the shops have many normal employees to run it without needing the manager's help, then this design decision would just make the manager’s interface more complicated, and we would consider separating their functions distinctively.    

### ADR06: Customer Lookup by Phone number
**Options:**
- By name
- By customer_id
- By phone number

***Chose:** By phone number    
**Why:** Normally nobody would use id to look up anything since it’s too difficult to remember, and there will be duplicates easily leading to mistakes in case there’re customers with the identical name. Instead, using phone numbers is a widely used method in many shops (for example: TH True Milk), when the cashiers only need to ask for their phone number and speak out their name to confirm once the recorded customer profile with that number is shown.    
**What would change our mind:** If our system expanded into a big e-commerce platform where frequent and clear contact or discussion with the customers is needed, then we would consider switching to email or customer accounts for them to log in and use.    
