# Process Dossier - Demand Forecasting Tool for Small Shop

## Section 1 - Chosen process and its position on the spectrum

### (a) The model

The hybrid Spiral working model will be used in this project, with the ratio of 90% Agile and 10% Plan-driven. The Spiral model helps us understand and reduce risks while focusing on planning, analysis, and critical thinking. The project requires structured planning to meet course deadlines (plan-driven), but most work follows Spiral's iterative, risk-based approach to adapt to evolving requirements.

#### Cycle overview

| Spiral | Order | Tasks | Output | Responsible roles |
|---|---:|---|---|---|
| | 1 | Defining the goals and objectives of this round | Prioritized task list | Project manager (Phương Oanh) |
| | 2 | Risk analysis | Risk register with corresponding solutions | Development & analysis team (Ánh Dương) |
| | 3 | Developing | Functional prototype | Developers (Ngọc Mai) |
| | 4 | Testing | Evaluation report including what is missing, pros, and cons | Testers & users (Hà Vy) |

At the end of each cycle, a tested prototype and an updated risk plan for the next iteration will be produced.

### (b) The position on the spectrum

The process sits closer to the plan created at the beginning of the project due to fixed semester milestones and deadlines, but primarily operates in Spiral mode to manage risks and adapt designs iteratively. Major project goals and timelines remain constant throughout the semester, while implementation details and technical decisions are revisited in each cycle.

## Section 2 - The five diagnostic questions

### 1. Are your requirements stable or volatile? What evidence do you have?

**Volatile, because:**

- As an F&B management application covering various functions, from products, orders, customers, to employees, some aspects such as function distribution for different roles and possible integration of weekly/monthly report exporting or payment management are not completely defined yet.
- Its target users include different types of workers in the F&B field, such as shop managers, stock managers, employees, cashiers, HR managers, and all-in-one shopkeepers. Therefore, diverse role-based functions may be needed in practice.
- The scale of shops using this application will be small, and their management and selling procedures may change rapidly, for example by adding vouchers, changing VIP customer management and discount policies, or exporting frequent sales reports.
- This project is currently at an experimental student level, with no actual F&B users to try and validate it. Therefore, changes are expected after feedback from internal testing and the instructor after the product is released.

### 2. Does the project carry safety or legal impact that would demand formal documentation and change control?

No, formal documentation might not be necessary.

- As a small-scale F&B management application, it is a local management tool for small shops and is not related to highly sensitive data such as medical, financial, or banking records.
- Its main users are workers of small F&B shops; therefore, system errors might not lead to severe legal consequences, although they could affect the shops' sales.
- The project has not yet been tested in real-life businesses, so there is no need for formal change-control procedures like those required in critical systems such as healthcare, banking, or government.

Therefore, only requirement and design documents at an academic level are needed. Formal documentation and change control are not required.

### 3. Is your team large and distributed, or small and co-located? How does that affect communication cost?

Our team has four members, so communication and coordination are relatively easy. However, parts such as data processing, forecasting models, and the user interface still need to work closely together. Therefore, we will communicate regularly and use GitHub and Pull Requests to track and review changes.

### 4. Can your customer engage continuously, or only at fixed checkpoints?

The instructor mainly provides feedback during classes, consultations, and project milestones. Any real users we consult may also have limited availability. Therefore, we will use prototypes and working demos to collect feedback at suitable checkpoints and make adjustments in later development cycles.

### 5. What do organizational culture and contract constraints allow?

The course has four fixed milestones and a final demo date, so our team needs a clear plan to stay on schedule. However, between milestones, we can still adjust task priorities, detailed requirements, and forecasting models based on actual results. This makes a hybrid Spiral process with Agile practices suitable for our project.

## Section 3 - Critical thinking: risks of the opposite choice

If our team used a fully plan-driven process instead of an Agile-oriented process, the biggest risk would be extensive rework caused by changing requirements. Our system has several user groups, including managers, store owners, and employees, whose needs may become clearer during development. Requirements such as product management, inventory management, employee management, and the user interface may also change as the team receives feedback.

In a fully plan-driven process, these requirements would be defined and fixed earlier, making later changes more costly. The first visible symptom would be unfinished or repeatedly modified features near a milestone, as the team would spend increasing amounts of time reworking functions that had already been implemented.

## Section 4 - Process rules your team commits to

1. Sprint length is one week, and the team will review and re-prioritize the backlog at the beginning of every sprint.
2. Every change to the `main` branch must be submitted through a Pull Request and reviewed by at least three other team members before merging.
3. Any requirement change after a sprint starts must be recorded in `docs/changelog.md`, including the changed requirement and the reason for the change.
4. New features are added to the backlog first and are only started after the team agrees on their priority.