#Milestone 1 - Requirements Document
##Product vision
**to be filled later**

##Personas
**to be filled later**

##Scenarios
**to be filled later**

##User stories
**@oanh please change the US number accordingly. This is just to note down the ideas.**
US06: Orders viewing - P0 - points: 5
As a manager, I want to see all the order lists, their payment status and their history so that all order information is clear to me even when I’m not the one who created them.
Acceptance criteria:
-Given that there are around 25 orders created by various employees of mine, when I open the order viewing interface under manager’s account, then I should see all 25 of them.
-Given that an order has 3 changes in its status (regardless of which employee did it), when I open its history, then I should see all 3 of them
Task:
--API/query to retrieve all orders at first
Page division: Display 15-20 orders each page
-Display an order’s detailed information, including its chronological history
-“Empty” state handling for no order case
-Test for all things above’s visibility and validation


US07: Order management - P0 - points: 5
As a manager, I want to be able to create, edit or confirm payment for orders like an employee could, so that I can do it myself when we’re short-staffed.
Acceptance criteria:
-Given that I’m on the order creating interface using my manager account, when I add at least 1 valid product into the list and create the order, then it should be successful.
-Given that the order is at before-payment status, when I receive the money from the customer and change its status into Paid, then it should be successful and the order should appear in the history.
Task:
-Order creating/editing form (same logic as Employee’s)
-Recalculate the total price after each addition/adjustment
-Payment confirmation - order’s payment status switching
-Order history record
-Test for validation


US08: Inventory management - P0 - points: 5
As a manager, I want to see all the inventory lists as well as add or edit a product so that I can make better plans for budget and sales control, instead of just preparing the ingredients based on intuitions.
Acceptance criteria:
-Given that there are 10 items in my shop’s inventory regardless if they're still available or we ran out of them, when I open the inventory interface, then I should see all 10 of them.
-Given that there’s an item with the current quantity of 5, when I restock them with 10 more of that item, then its quantity should become 15.
Task:
-Retrieve the whole inventory list to display product’s name, quantity or date, etc.
-Product addition/editing form (with quantity and date validation)
-Empty-stock handling when there’s no item in inventory
-Test for validation


US09: Expiry date warning - P0 - points: 5
As a manager, I want to have an expiry date warning mechanism so that I can know which product is expired to dispose of.
Acceptance criteria:
-Given that there is an item which has been stocked in our inventory, when it stays there for 7 days without being sold - which, to us, is too long for it to remain edible, then it should be labeled as “Expired”.
-Given that an item is labeled as “Expired”, when I view the inventory, then it should appear more visually noticeable or highlighted so I can notice and handle it as soon as possible.
-Given that an item is labeled as “Expired”, when I view the inventory, then it should be hidden from the ready-to-sell list so we won’t sell spoiled products to customers.
Task:
-Auto-assign Expired label based on stocking date
-Show Expired label in a certain style to ensure noticeability
-Exclude expired products from sellable list
-Test for validation


US10: Low-stock warning - P0 - points: 5
As a manager, I want to have a low-stock warning mechanism so that I can know what is short and important in time.
Acceptance criteria:
-Given that there is an item whose quantity is only 3, when I view the inventory, then it should be highlighted as “Low-stock” so I can restock it as soon as possible.
-Given that I restock a low-stock item, when its new quantity is over 3, then the “Low-stock” label on it should disappear.
Task:
-Configure minimum stock quantity for each product
-Implement low-stock calculation based on each product’s current quantity and its minimum stock quantity
-Display “Low-stock” label and handle its visibility when the quantity changes
-Test for validation


US11: Sale and profit dashboard - P0 - points: 5
As a manager, I want to generate a dashboard of sales and profit, as well as analysis of it, so that I can get the information saved without having to use printed tickets and physical notebooks.
Acceptance criteria:
-Given that my shop has been active for more than 7 days, when I require a weekly sales report, then I should be able to get a dashboard of the latest 7 days.
-Given that my shop hasn’t been active for enough 28-30 days, when I require a monthly sales report, then I should receive a notification of “Not enough information to generate”.
Task:
-Implement sales revenue calculation
-Create visualizations (line, bar chart, etc.)
-Handle empty-state when there’s not enough information to create required dashboard
-Test for date/week/month filtering


US12: Customer management - P0 - points: 5
As a manager, I want to see all traditional (dine-in, takeaway) customer lists, including their purchase history, loyalty, etc. as well as add or edit customers so that I can save all of their information, since online F&B markets are the only way we can track a customer’s history.
Acceptance criteria:
-Given there are 50 customers via different traditional ordering channels (dine-in, takeaway, etc.), when I view my customer list, all 50 of them should appear.
-Given that a customer has purchased in our shop 10 times, when I view that customer’s order history/loyalty tracking, all 10 past orders of them should appear.
-Given that a customer’s profile already exists in the system, when I mistakenly add them as a new customer, then I should see the notification “Duplicated customer”.
Task:
-Display customer’s information page with their purchase history
-New customer addition/existing customer editing form
-Implement loyalty tracking based on their total purchase time.
-Empty-state handling when there’s no recorded customer yet or a customer without purchase history
-Test for validation


US13: Membership tier assignment - P0 - points: 5
As a manager, I want an automatically assigned membership tiers mechanism based on their spending, so that I can save time on assigning them manually.
Acceptance criteria:
-Given that the membership threshold (based on money spent) is >50$ for Bronze, >100$ for Silver and >150$ up for Gold, when a customer spends a total of 52$ on my shop, then they should be recorded as a Bronze customer.
-Given that the customer above spends 110$ total on my shop, when the system recalculates their tier, then it should be upgraded to Silver.
Task:
-Assign membership based on each customer’s recorded spent money
-Auto-upgrade customers’ tier when their spending reaches a new threshold
-Auto-recalculate customers’ total spending after each successful purchase
-Test for validation


US14: Employee management - P0 - points: 5
As a manager, I want to be able to add or edit an employee or view my employees list, so that I can handle my shop’s human resource digitally without using physical notebooks.
Acceptance criteria:
-Given that my shop has 15 active employees, when I open the employee management interface, then all 15 of them should appear.
-Given that an employee’s profile already exists in the system, when I mistakenly add them as a new employee, then I should see the notification “Duplicated employee”.
-Given that I haven’t finished the form when adding a new employee, when I try to submit, then a notification of missing information should appear.
-Given that an employee’s role is “Regular employee”, when I change their role into “Cashier”, their role displayed in the system should change accordingly.
Task:
-Display employee’s information page with their details
-New employee addition/existing employee editing form
-Empty-state handling when there’s no employee yet
-Test for validation