# Daily

## 16/09/2026
- @aizun: received tasks #18 and created task #19 and 5 other sub-issues. wrote questions and answer-form, ready to conduct surveys tmr.

## 17/09/2026
- @aizun: conducted 2 interviews. recorded into audios. wrote the answers in answers forms.

## 18/09/2026
- @ngocmai141106: Switched the task into In progress. Filled in the basic idea for manager's US. No acceptance criteria nor Task included yet. The file is unbeta-ed.

## 19/09/2026
- @ngocmai141106: Finished manager's US part. Priority and assigned point be decided later.
- @oanhtran020906-sys: filled in the idea for employee's US with priority and points assigned to each one.
- @oanhtran020906-sys: added 6 business rules.
- @ngocmai141106: Added screenlist t Screen and Flow part.
- @HaVy2006: contributed to refining the screen/flow design for Milestone 1.

## 25/09/2026
- @HaVy2006: started working on the frontend prototype for YUMS. Built the Home page and completed most of the sidebar navigation and layout.

## 27/09/2026
- @aizun: created basic tasks for sprint 2, focused on database; update sprint 2 documents
- @HaVy2006: Contiued to built the 404 page and navigation flow.

## 01/10/2026
- @HaVy2006: started designing the data model for YUMS. Worked on identifying the required tables, attributes, primary keys, foreign keys, and relationships based on the requirements. 

## 02/10/2026
- @ngocmai141106: Finished pushing all required files for Order interfaces. Finished the Design decisions part in the design file.
- @oanhtran020906-sys: add inventory page
- @oanhtran020906-sys: add sales and profit dasboard and demand prediction and restock suggestion in sales page
- @aizun: completed demo frontend for employee pages. need to add an kpi employee page. edit the customer pages. need to study about architecture, api. ughhh i'm suffering ToT these deadlines and requirements are too much, too urgent!!! imma oej oej
- @oanhtran020906-sys: add inventory page
- @HaVy2006: revised the data model based on feedback from team members and implemented database logic such as invoice total calculation and related business rules. Completed around 80% of the database schema and seed data. This job is truly exhausting. 
- @aizun: 2nd daily update... i have fixed the customer FE pages, fix bug of database/seed.sql, and so much more that i can't remember at 10:35pm. this Sprint is truly madness!!! Tomorow, i will do some research about architecture, API design, then write to the official docs. then i will plan to write all the python backend, api, so the web can function so real. hopefully we can made it on Sunday night. Ugh! the workload of this sprint is just tooooo much ToT doing not only the design, but also make a running app (though just partial) in only 5 days????? like we only knew what to do on this Wed-30/09/26. 

## 03/10/2026
- @ngocmai141106: Fixed order payment into order delivery status since we've agreed that there was no need to separate into 3 payment status like that while only Success contributes to the sales and the rest will just be database's trash. Delivery status (means the employees at the counter has given the drinks/food to the customer yet) makes much more sense. All the related information in requirements.md (including US, screen list, diagram) have also been fixed accordingly. Demand & Stock prediction function has also been added as a child screen of /sales, as we were reminded by the instructors that our core function - prediction had been neglected. This has been added as new USs by @oanhtran020906-sys before, and has been fixed accordingly in screen list and UC diagram. Old diagram (both png and xml forms) has been replaced by the new version. @oanhtran020906-sys please notice this message while writing What changed in part in this sprint's design.md file.
- @aizun: watched 2 youtube videos about software architecture and read 1 chapter of a book about layered pattern. i drew the architecture diagram with Canva, not sure if that is meet the lecturer's requirements, but it looks pleasing and giving a sweet, candies vibe UwU. I also listed out the basic functions and write the API design table. I'm stil wondering about how to update the product price, that's very complicated and need further discussions.
- @HaVy2006: started writing the data model and Walking Skeleton sections in the Sprint 2 documentation. Decided to use the employee management route for the Walking Skeleton and discussed the approach with the team.
- @HaVy2006: Later found that the database was missing the `users` table, so updated the ERD and database model accordingly.

## 04/10/2026
- @oanhtran020906-sys: add section 6: what changed in this sprint since M1, write in file design.md. write what changed, why it changed, what was added, impact
- @aizun: what a exhausting afternoon. i created the file to initialise the databse (init_db.py) for the first time device, and i had to delete all of the progress and do it all over again cuz the 1st time was a huge failure. also rewrote the connect_db.py cuz it was not look like a callable function, fix bug: standardize the seed file . wrote the employee services to get all from employee table, add new, and update employee just for the demo.haizzzz after that i had to change frontend html and js to use the written APIs. Of course, as the one who wrote all of that, i wrote SETUP.md as an instruction. sprint-log is waiting. i think we are ready to submit milestone 2. i know the lecturer won't read these line so... ugh this sprint's workload is just too much, it drained my weekend, and i could not hang out T^T Please consider to reduce the workload or extend the deadlines, we have other 5 subjects to work on. but hey 'kẻ mạnh không đổ tại hoàn cảnh, kẻ mạnh đạp lên hoàn cảnh!'. Silly words =))) but your mind can't give clear words in this tiring condition.
- @oanhtran020906-sys: add information of the tester in design.md, update commits in sprint log
- @HaVy2006: completed the Sprint 2 database and Walking Skeleton work, i changed the docs a little bit because we use 3 routes: add an employee, update an employee and show employee list. Successfully connected Python with MySQLand finished the required documentation and screenshots for Milestone 2.

## 10/10/2026
- @ngocmai141106: Fixed the Priority of the two order screens i mixed up in requirements.md. @aizun (are you or sb else?) pls notice if you need to write this in this sprint's What changed.