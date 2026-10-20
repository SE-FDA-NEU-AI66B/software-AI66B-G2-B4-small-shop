# YUMS — UI Documentation (M3)

## 1. PO Stories and Screen Flow

### 1.1 PO Stories

| User Story | Screen | Route | Status | Related Issue |
|---|---|---|---|---|
| US01 - Create an order | Order Directory (New order tab) | `/order` | partly works - it’s fine by our old logic in linking a to-be-created order to a customer, but not by our new logic of this problem. Will fix this once the code is fixed. | #198 |
| US02 — Confirm delivery status | Order Directory (Check order tab) | `/order/check/{id}/deliver` | partly works - we’ve agreed that an order should have multiple delivery status rather than multiple payment status, but it’s still working by payment status, where Success = successful in payment + delivered | #199 |
| US06 - View all orders | Order Directory (Check order tab) | `/order/check` | works | #203 |
| US15 Demand forecasting | Sales & Demand Analytics | `/sales` | works | #205 |
**Status:** Not Started / In Progress / Completed

### 1.2 Screen Flow Diagram

<!-- Add or update the screen-flow diagram here. -->

![Screen Flow Diagram](images/ui/order_flow.png)

---

## 2. UI Wireframes

Document every screen related to the PO user stories.

### 2.1 [Create an Order]

**Related User Story:** US01 — [Create an order]

**Purpose:**  
The user comes here to create a new order by choosing dishes and quantity, sum them up and confirm the customer’s payment.

**Route:**  
`/order`

**API Endpoints:**

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/products` | Fetch products to display on the selection area |
| GET | `/api/customers/search?phone=<number>` | Fetch the customer(s) with the phone number the order creator is trying to search |
| POST | `api/orders` | Create new order |

**Wireframe:**

![Order creation - Wireframe](images/ui/order_create_wire.png)
![Order creation - Real UI](images/ui/order_create_real.png)

### 2.2 [Confirm Delivery Status]

**Related User Story:** US02 — [Confirm an order's delivery status]

**Purpose:**  
The user comes here to confirm an already-created order’s delivery status by changing it from Not delivered to Delivered.

**Route:**  
`/order/check/{id}/deliver`

**API Endpoints:**

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `api/orders/{id}` | Fetch the order with that particular id's information |
| PATCH | `/order/check/{id}/deliver` | Change that order's delivery status

**Wireframe:**

![Order delivery status - Wireframe](images/ui/order_deliver_wire.png)

### 2.3 [View All Orders]

**Related User Story:** US01 — [View all orders]

**Purpose:**  
The user comes here to view previously created orders and their basic information.

**Route:**  
`/order/check`

**API Endpoints:**

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `api/orders` | Fetch all orders |

**Wireframe:**

![Order creation - Wireframe](images/ui/order_check_wire.png)
![Order creation - Real UI](images/ui/order_check_real.png)
---

### 2.1 US15 — Demand Forecasting & Restock Alert (4 States)

The user comes here to analyze historical sales rates, predict inventory demand for the next 7, 14, or 30 days, and identify critical stock deficit risks.

**Route:** `/sales`  
**Calls:** `GET /api/sales/overview`, `GET /api/sales/predictions`
```
+-- Empty ---------------------+  +-- Loading -------------------+
|                              |  |                              |
|   No inventory forecast data |  |          (spinner)           |
|      available to display.   |  |   Calculating demand...      |
|                              |  |    [====================]    |
+------------------------------+  +------------------------------+
+-- Error ---------------------+  +-- Data ----------------------+
|                              |  | Item: Oolong Milk Tea        |
|  Failed to load forecast data|  | Current Stock: 15 items      |
|        [ Try again ]         |  | Forecast (30d): 420 items    |
|                              |  | Alert: Restock Needed (+415) |
+------------------------------+  +------------------------------+
```
![Demand Forecasting - Real UI](images/ui/demand_real_ui.png)

---
## 3. User-Friendly Error Messages

Document at least four error messages mapped to actual API error codes and business rules.

| # | Related User Story | API Error Code | Business Rule | User-Friendly Message | Suggested Action |
|---|---|---|---|---|---|
| 1 | US01 | 409 | BR1 | This product is insufficient at the moment! | Choose another product that is not ran out |
| 2 | US01 | 409 | BR4 | This product is expired and cannot be sold! | Choose another product that is still edible |
| 3 | US01 | 422 | BR10 | An order must contain at least one product! | Make sure to click at least one dish before clicking "Sum" |
| 4 | US02 | 409 | BR2 | Your already confirmed this order's delivery status! | Only change a Not Delivered order's delivery status. Or "Deliver" button won't appear on already-delivered orders at all |
| 9 | US15 | 400 | BR11 | Invalid forecasting window selected! | Choose a valid window option from 7, 14, or 30 days |
| 10 | US15 | 404 | BR12 | No category records found matching your filter! | Clear or change your category search keywords |
| 11 | US15 | 500 | BR15 | Unable to calculate demand prediction! | Contact system administrator to verify historical sales data |
| 12 | US15 | 403 | BR01 | Access denied to sales analytics page! | Log in with an Administrator or Store Manager account |
**Notes:**
- Use error codes that actually exist in the API/backend.
- Link each error to the relevant business rule.
- Write messages in language that users can understand.
- Explain what the user can do next.
- Do not invent error codes or business rules.

---

## 4. Changes Since M2

Describe the UI changes made since Milestone 2 and explain why they were needed.

### Change 1 — [Change Title]

**Before M3:**  
TODO: Describe the previous design.

**After M3:**  
TODO: Describe the updated design.

**Reason for Change:**  
TODO: Explain the problem or feedback that motivated the change.

**Impact on Users:**  
TODO: Explain how the change improves usability or supports a user story.

**Evidence:**

![Updated UI](images/ui/updated-screen.png)

<!-- Repeat for additional changes if applicable. -->

**Design Document:**  
See [`design.md`](design.md) for the corresponding UI design change.

---

## 5. References

- UI wireframes and screenshots: `docs/images/ui/`
- UI design decisions: `docs/design.md`
- Setup instructions: `docs/SETUP.md`
- Project user stories: TODO: Link to the relevant requirements document
