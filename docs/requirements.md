# Milestone 1 - Requirements Document
## Product vision
YUMS (YoU Manage your Shop) is a management website designed for small food and beverage (F&B) shop owners. It provides a centralized system to handle day-to-day operations, long-term information tracking, and specially customized to fit small shops' requirements and preferences in simplicity.

## Personas    

**1. My Doan, shop manager of Rot Rot cafe, 24**
Ms Doan is a shop manager of a take-away coffee shop. She stays at the shop the entire day through all 3 shifts. She makes coffee, buys ingredients, and supervises her employees. She use notebooks and a selling app from iPOS to manage the store. 
- Goal: Manage employees and inventory simply, can get rid of physical notebooks.
- Pain: The current selling app does not provide enough features, keeping multiple notebooks for each mission.
- In her words: *"I'm keeping multiple notes, and that's messy"* (interviewed on 17th Sep 2026).
- Technical skills: very familiar, use both phone, laptop, selling machines from iPOS.

**2. Viet, shop owner of Banh Trang Be My, 33**
Mr Viet is a shop owner of a branch store of Banh Trang Be My. He and his wife make contact with other siblings on Group chat to report financial condition and to provide ingredients. His shop serve both take-away and dine-in. He use a selling system so the customers can make orders by scanning a QR code on the table. 
- Goal: A clear and precise revenues and profit reports with visualization.
- Pain: The current app does not provide tracking expenses. He can only see the total revenue but cannot calculate the profit.
- In his words: *"This is just a selling app, not a managing app so it doesn't have the expenses tracking"* (interviewed on 17th Sep 2026).
- Technical skills: basic, phone only, doesn't have a laptop.

**3. Linh, employee of Ot Chuong Mart, 42**
Mrs Linh is a part-time cashier of Ot Chuong Mart. She sits at the cashier desk, create bills on a computer, and some times check inventory at the end of the day. The mart is crowded most of the time, so the queue is usually quite long.
- Goal: make payment for each customer as quick and simple as possible.
- Pain: the names of the products are weird, hard to remember to lookup in the system. Creating new customer may take time, lenghthen the waiting time of the queue.
- In her words: *"but if there's a long queue, asking every single customer for their phone number would take lots of time and the waiting customer would be mad and make complaints."* 
- Technical skills: as a middle-age, she struggles with technology, required training before she hiring.


## Scenarios    
**1. My Doan checks for Inventory**
1. At the end of the day, Ms Doan wants to check for expired ingredients.
2. She opens the app, check the *'Inventory'* section.
3. The app shows all the ingredients she is having, bought date and expired date, with warning flags.
4. She select the *'expired'* products, the app shows a list.
5. She takes the expired ingredients from the fridge and the counter, destroy them.
6. She comes back the the app, press *'destroyed all'* (or select what she has destroyed)
7. The app shows pop-ups, confirm, and delete the destroyed products/ingredients.

**2. Viet calculates the profit**
1. Viet buying the ingredients to prepare for today.
2. He opens the *'Sales'* section, note down the expenses, the cost of his shopping.
3. The app confirms his expenditure. He close the app.
4. After a long day, all the orders and revenue are recorded. He open the *'Sales* section again.
5. The app shows the dashboards, numbers, calculated profit, revenue, expenses on the top of the page.
6. He saw the report, feels happy with eye-pleasing charts, press *'Export Dashboard'*.
7. The system download an image or a PDF file of the dashboard to his device, and show confirms.

**3. Linh creates a new customer profile**
1. Linh is checking out for this new customer, before they pay, she asks for the customer's information.
2. She press *'New customer'* button right on the order page.
3. The app shows the boxes, input bars,... for Linh to write the customer's details in.
4. She writes the customer info.
5. She doubled checks, and press *'Confirm'*
6. The app shows notification of success, the new customer has been saved to the system.


## User stories 
### US01: Order creation - P0 - points: 5

As an employee, I want to create and edit an order by searching or scanning products so that I can process a customer's purchase quickly and accurately.

***Acceptance criteria:***

- Given that there is a valid product in the shop's inventory, when I scan its barcode or search for it by item name/category code, then the product should be added to the current order.

- Given that an order already contains 2 products, when I add 1 more valid product or adjust its quantity, then the order should display 3 products with the updated total price.

- Given that I try to add a product which is unavailable for sale, when I add it to the order, then the system should reject it and display the message “Product is not available”.

***Task:***

- Product search by item name/category code

- Barcode scanning

- Add/remove product from current order

- Adjust product quantity

- Recalculate total price after each addition/adjustment

- Prevent unavailable products from being added

- Test for order creation/editing and validation

### US02: Order payment - P0 - points: 5

As an employee, I want to confirm an order's payment so that I can complete the customer's purchase and record its payment status.

***Acceptance criteria:***

- Given that an order is at “Before-payment” status, when I receive the customer's payment and confirm it, then the order status should change to “Paid”.

- Given that an order has a total price of $25, when I confirm that the customer has paid $25, then the order should be successfully marked as “Paid”.

- Given that an order is still at “Before-payment” status, when I try to complete it without confirming payment, then the order should remain at “Before-payment”.

***Task:***

- Display current order total

- Payment confirmation

- Order payment-status switching

- Prevent completion without payment confirmation

- Record successful payment in order history

- Test for payment validation

### US03: Order history - P1 - points: 3

As an employee, I want to view my previous orders and their payment status so that I can review the orders I have processed during my shifts.

***Acceptance criteria:***

- Given that I have processed 10 orders, when I open my order history, then I should see all 10 orders that were created or processed by my account.

- Given that one of my previous orders has a payment status of “Paid”, when I open that order's details, then its payment status should be displayed as “Paid”.

- Given that I have not processed any orders yet, when I open my order history, then I should see an empty state indicating that there are no previous orders.

***Task:***

- Retrieve orders associated with the current employee account

- Display order list with order ID, date/time, total price and payment status

- Display an order's detailed information

- Display chronological order/payment history

- Handle empty state when the employee has no previous orders

- Test order filtering and information visibility

### US04: Customer lookup and loyalty - P0 - points: 5

As an employee, I want to search for a customer by phone number and see their loyalty information so that I can apply their customer information while processing an order.

***Acceptance criteria:***

- Given that a customer with phone number “0123456789” already exists, when I search for that phone number, then the system should display the customer's name, reward points and purchase history.

- Given that a customer has 10 previous purchases, when I open their purchase history, then all 10 previous purchases should be displayed.

- Given that no customer exists with the searched phone number, when I search for it, then the system should display a “Customer not found” state and allow me to enter the customer's name to create a profile.

***Task:***

- Customer search by phone number

- Display customer profile

- Display reward/loyalty information

- Display purchase history

- Handle customer-not-found state

- Allow new customer information to be entered when necessary

- Test for search and validation

### US05: Receipt printing - P1 - points: 3

As an employee, I want to print a receipt after an order is paid so that I can provide the customer with a record of their purchase.

***Acceptance criteria:***

- Given that an order has been successfully marked as “Paid”, when I select the print receipt action, then the system should generate a receipt containing the order's products, total price and payment status.

- Given that an order has not been paid, when I try to print its receipt, then the system should prevent the receipt from being generated as a completed purchase receipt.

***Task:***

- Receipt generation

- Display purchased products and quantities

- Display total price and payment status

- Prevent receipt printing for unpaid orders

- Test receipt visibility and validation

### US06: Orders viewing - P0 - points: 5    
As a manager, I want to see all the order lists, their payment status and their history so that all order information is clear to me even when I’m not the one who created them.    

***Acceptance criteria:***
- Given that there are around 25 orders created by various employees of mine, when I open the order viewing interface under manager’s account, then I should see all 25 of them.    
- Given that an order has 3 changes in its status (regardless of which employee did it), when I open its history, then I should see all 3 of them.    

***Task:***    
- API/query to retrieve all orders at first    
- Page division: Display 15-20 orders each page    
- Display an order’s detailed information, including its chronological history    
- “Empty” state handling for no order case    
- Test for all things above’s visibility and validation    


### US07: Order management - P1 - points: 3   
As a manager, I want to be able to create, edit or confirm payment for orders like an employee could, so that I can do it myself when we’re short-staffed.    

***Acceptance criteria:***    
- Given that I’m on the order creating interface using my manager account, when I add at least 1 valid product into the list and create the order, then it should be successful.    
- Given that the order is at before-payment status, when I receive the money from the customer and change its status into Paid, then it should be successful and the order should appear in the history.    

***Task:***    
- Order creating/editing form (same logic as Employee’s)    
- Recalculate the total price after each addition/adjustment    
- Payment confirmation - order’s payment status switching    
- Order history record    
- Test for validation    


### US08: Inventory management - P0 - points: 5    
As a manager, I want to see all the inventory lists as well as add or edit a product so that I can make better plans for budget and sales control, instead of just preparing the ingredients based on intuitions.    

***Acceptance criteria:***
- Given that there are 10 items in my shop’s inventory regardless if they're still available or we ran out of them, when I open the inventory interface, then I should see all 10 of them.    
- Given that there’s an item with the current quantity of 5, when I restock them with 10 more of that item, then its quantity should become 15.    

***Task***:    
- Retrieve the whole inventory list to display product’s name, quantity or date, etc.    
- Product addition/editing form (with quantity and date validation)
- Empty-stock handling when there’s no item in inventory
- Test for validation


### US09: Expiry date warning - P1 - points: 3   
As a manager, I want to have an expiry date warning mechanism so that I can know which product is expired to dispose of.    

***Acceptance criteria:***
- Given that there is an item which has been stocked in our inventory, when it stays there for 7 days without being sold - which, to us, is too long for it to remain edible, then it should be labeled as “Expired”.
- Given that an item is labeled as “Expired”, when I view the inventory, then it should appear more visually noticeable or highlighted so I can notice and handle it as soon as possible.
- Given that an item is labeled as “Expired”, when I view the inventory, then it should be hidden from the ready-to-sell list so we won’t sell spoiled products to customers.

***Task:***
- Auto-assign Expired label based on stocking date
- Show Expired label in a certain style to ensure noticeability
- Exclude expired products from sellable list
- Test for validation


### US10: Low-stock warning - P1 - points: 3    
As a manager, I want to have a low-stock warning mechanism so that I can know what is short and important in time.    

***Acceptance criteria:***
- Given that there is an item whose quantity is only 3, when I view the inventory, then it should be highlighted as “Low-stock” so I can restock it as soon as possible.
- Given that I restock a low-stock item, when its new quantity is over 3, then the “Low-stock” label on it should disappear.

***Task:***
- Configure minimum stock quantity for each product
- Implement low-stock calculation based on each product’s current quantity and its minimum stock quantity
- Display “Low-stock” label and handle its visibility when the quantity changes
- Test for validation


### US11: Sale and profit dashboard - P0 - points: 5    
As a manager, I want to generate a dashboard of sales and profit, as well as analysis of it, so that I can get the information saved without having to use printed tickets and physical notebooks.    

***Acceptance criteria:***
- Given that my shop has been active for more than 7 days, when I require a weekly sales report, then I should be able to get a dashboard of the latest 7 days.
- Given that my shop hasn’t been active for enough 28-30 days, when I require a monthly sales report, then I should receive a notification of “Not enough information to generate”.

***Task:***
- Implement sales revenue calculation
- Create visualizations (line, bar chart, etc.)
- Handle empty-state when there’s not enough information to create required dashboard
- Test for date/week/month filtering


### US12: Customer management - P1 - points: 3   
As a manager, I want to see all traditional (dine-in, takeaway) customer lists, including their purchase history, loyalty, etc. as well as add or edit customers so that I can save all of their information, since online F&B markets are the only way we can track a customer’s history.    

***Acceptance criteria:***
- Given there are 50 customers via different traditional ordering channels (dine-in, takeaway, etc.), when I view my customer list, all 50 of them should appear.
- Given that a customer has purchased in our shop 10 times, when I view that customer’s order history/loyalty tracking, all 10 past orders of them should appear.
- Given that a customer’s profile already exists in the system, when I mistakenly add them as a new customer, then I should see the notification “Duplicated customer”.    

***Task:***
- Display customer’s information page with their purchase history
- New customer addition/existing customer editing form
- Implement loyalty tracking based on their total purchase time.
- Empty-state handling when there’s no recorded customer yet or a customer without purchase history
- Test for validation


### US13: Membership tier assignment - P1 - points: 3    
As a manager, I want an automatically assigned membership tiers mechanism based on their spending, so that I can save time on assigning them manually.    

***Acceptance criteria:***
- Given that the membership threshold (based on money spent) is >50$ for Bronze, >100$ for Silver and >150$ up for Gold, when a customer spends a total of 52$ on my shop, then they should be recorded as a Bronze customer.
- Given that the customer above spends 110$ total on my shop, when the system recalculates their tier, then it should be upgraded to Silver.    

***Task:***
- Assign membership based on each customer’s recorded spent money
- Auto-upgrade customers’ tier when their spending reaches a new threshold
- Auto-recalculate customers’ total spending after each successful purchase
- Test for validation


### US14: Employee management - P1 - points: 3   
As a manager, I want to be able to add or edit an employee or view my employees list, so that I can handle my shop’s human resource digitally without using physical notebooks.    

***Acceptance criteria:***
- Given that my shop has 15 active employees, when I open the employee management interface, then all 15 of them should appear.
- Given that an employee’s profile already exists in the system, when I mistakenly add them as a new employee, then I should see the notification “Duplicated employee”.
- Given that I haven’t finished the form when adding a new employee, when I try to submit, then a notification of missing information should appear.
- Given that an employee’s role is “Regular employee”, when I change their role into “Cashier”, their role displayed in the system should change accordingly.    

***Task:***
- Display employee’s information page with their details
- New employee addition/existing employee editing form
- Empty-state handling when there’s no employee yet
- Test for validation

## Business Rules
### BR1: Unavailable products cannot be added to an order

A product that is unavailable for sale must not be added to a new or existing order.

***Worked example:***
A product is marked as unavailable. When an employee tries to add it to an order, the system rejects the action and displays “Product is not available”.

### BR2: An order cannot be completed before payment is confirmed

An order with “Before-payment” status must remain incomplete until its payment has been confirmed.

***Worked example:***
An order is currently “Before-payment”. When an employee tries to complete the order without confirming payment, the order remains “Before-payment”.

### BR3: Only paid orders can be printed as completed purchase receipts

The system must not generate a completed-purchase receipt for an order that has not been marked as “Paid”.

***Worked example:***
An order is still “Before-payment”. When an employee tries to print its receipt, the system prevents the receipt from being generated as a completed purchase receipt.

### BR4: Products kept for 7 days without being sold are considered expired

A product that remains in inventory for 7 days without being sold must be labeled “Expired” and excluded from the ready-to-sell list.

***Worked example:***
An item has been stocked for 7 days and has not been sold. The system labels it “Expired” and hides it from the ready-to-sell list.

### BR5: Products at or below the minimum stock quantity are considered low-stock

A product must be labeled “Low-stock” when its current quantity reaches or falls below its configured minimum stock quantity. The label must disappear when its quantity is above that threshold.

***Worked example:***
A product has a minimum stock quantity of 3. When its quantity is 3, the system displays “Low-stock”. After restocking it to 4, the label disappears.

### BR6: Customer membership tier is determined by total spending

A customer's membership tier must be automatically assigned according to their recorded total spending:

- Bronze: > $50
- Silver: > $100
- Gold: > $150

***Worked example:***
A customer has spent $52 in total, so the system assigns Bronze. When their total spending reaches $110, the system upgrades them to Silver.

## Screens and flow
Note: E = employee; M = manager.    

| # | Route | Purpose | Access | Priority |
|---|-------|---------|--------|----------|
| 01 | /login | Login the system (with the right role). | E M | P0 |
| 02 | /order | Defaultly show the order list - how many based on the role, and access to other functional buttons. | E M | P1 |
| 03 | /order/new | Create new order. | E M | P0 |
| 04 | /order/{id} | View an order’s detailed information. | E M | P1 |
| 05 | /order/{id}/paymen | Switch and unpaid order to Paid status. | E M | P0 |
| 06 | /inventory | Defaultly show all inventory items with some basic information (and label if any). | M | P0 |
| 07 | /inventory/new | Add new items to the inventory. | M | P0 |
| 08 | /inventory/{id} | View an item’s detailed information. | M | P1 |
| 09 | /inventory{id}/edit | Edit an item’s information, including expiry date and low-stock threshold. | M | P0 |
| 10 | /inventory/{id}/delete | Delete an item. | M | P0 |
| 11 | /sales | Show daily/weekly/monthly sales reports. | M | P0 |
| 12 | /customer | Defaultly show all customers with some basic information. | M | P1 |
| 13 | /customer/new | Add new customers to the inventory. | M | P0 |
| 14 | /customer/{id} | View a customer’s detailed information. | M | P1 |
| 15 | /customer/{id}/edit | Edit a customer’s information (except their membership tier and spent money). | M | P0 |
| 16 | /customer/{id}/delete | Delete a customer. | M | P0 |
| 17 | /employee | Defaultly show all employees with some basic information. | M | P1 |
| 18 | /employee/new | Add new employees to the inventory. | M | P1 |
| 19 | /employee/{id} | View an employee’s detailed information. | M | P1 |
| 20 | /employee/{id}/edit | Edit an employee's information. | M | P1 |
| 21 | /employee/{id}/delete | Delete an employee. | M | P1 |

![](https://github.com/SE-FDA-NEU-AI66B/software-AI66B-G2-B4-small-shop/blob/29-draw-flow-login/docs/images/flow_login.jpg) 
![](https://github.com/SE-FDA-NEU-AI66B/software-AI66B-G2-B4-small-shop/blob/29-draw-flow-login/docs/images/flow_order.jpg) 
![](https://github.com/SE-FDA-NEU-AI66B/software-AI66B-G2-B4-small-shop/blob/29-draw-flow-login/docs/images/flow_inventory.jpg) 
![](https://github.com/SE-FDA-NEU-AI66B/software-AI66B-G2-B4-small-shop/blob/29-draw-flow-login/docs/images/flow_customer.jpg)
![](https://github.com/SE-FDA-NEU-AI66B/software-AI66B-G2-B4-small-shop/blob/29-draw-flow-login/docs/images/flow_employee.jpg) 
