# YUMS — UI Documentation (M3)

## 1. PO Stories and Screen Flow

### 1.1 PO Stories

| User Story | Screen Name | Route | Status | Related Issue |
|---|---|---|---|---|
| USXX — Story title | Screen name | `/route` | TODO | #XX |
| USXX — Story title | Screen name | `/route` | TODO | #XX |

**Status:** Not Started / In Progress / Completed

### 1.2 Screen Flow Diagram

<!-- Add or update the screen-flow diagram here. -->

![Screen Flow Diagram](images/ui/screen-flow.png)

---

## 2. UI Wireframes

Document every screen related to the PO user stories.

### 2.1 [Screen Name]

**Related User Story:** USXX — [Story title]

**Purpose:**  
TODO: Explain what users can accomplish on this screen.

**Route:**  
`/your-route`

**API Endpoints:**

| Method | Endpoint | Purpose |
|---|---|---|
| GET/POST/PUT/DELETE | `/api/your-endpoint` | TODO |

**Main UI Components:**
- TODO: Component 1
- TODO: Component 2
- TODO: Component 3

**User Actions:**
1. TODO: Describe the user action.
2. TODO: Describe the expected result.

**Wireframe:**

![Screen Name](images/ui/your-screen.png)

### 2.2 [Next Screen Name]

<!-- Repeat Section 2.1 for each screen in the PO user stories. -->

---

## 3. UI States

At least one screen must document all four states below.

**Screen:** TODO: Screen name

| State | Expected UI Behavior | User Action |
|---|---|---|
| Empty | Explain that no data is available. | TODO |
| Loading | Show a loading indicator while fetching data. | Wait for the request to complete. |
| Error | Display a user-friendly error message. | Retry or follow the suggested action. |
| Data | Display the retrieved data and available actions. | TODO |

**Evidence / Wireframes:**

- Empty: `images/ui/screen-empty.png`
- Loading: `images/ui/screen-loading.png`
- Error: `images/ui/screen-error.png`
- Data: `images/ui/screen-data.png`

<!-- Use actual image files and remove states that are not represented by real evidence only if the requirement permits. -->

---

## 4. User-Friendly Error Messages

Document at least four error messages mapped to actual API error codes and business rules.

| # | Related User Story | API Error Code | Business Rule | User-Friendly Message | Suggested Action |
|---|---|---|---|---|---|
| 1 | USXX | TODO | TODO | TODO | TODO |
| 2 | USXX | TODO | TODO | TODO | TODO |
| 3 | USXX | TODO | TODO | TODO | TODO |
| 4 | USXX | TODO | TODO | TODO | TODO |

**Notes:**
- Use error codes that actually exist in the API/backend.
- Link each error to the relevant business rule.
- Write messages in language that users can understand.
- Explain what the user can do next.
- Do not invent error codes or business rules.

---

## 5. Changes Since M2

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

## 6. References

- UI wireframes and screenshots: `docs/images/ui/`
- UI design decisions: `docs/design.md`
- Setup instructions: `docs/SETUP.md`
- Project user stories: TODO: Link to the relevant requirements document
