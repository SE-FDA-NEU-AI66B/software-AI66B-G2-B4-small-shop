# Milestone 5 - Operation Guie
## 1. How to run and release
### 1.1 The URL and platform
[Public frontend URL](https://yums-frontend-qjq2.onrender.com)    
[Public backend URL](https://small-shop-tailscale.onrender.com)    
[Health check link](https://small-shop-tailscale.onrender.com/health)    
(The frontend communicates with the backend via its public Render link, while the backend connects to MySQL database.)    
Hosting platform: Render and Tailscale    
Source repository: GitHub's software-AI66B-G2-B4-small-shop's. Main branch.
[Repository link](https://github.com/SE-FDA-NEU-AI66B/software-AI66B-G2-B4-small-shop)    

### 1.2. How a new version gets there
This is how a new version gets updated to the public web:
1. Us developers create a side branch and work there.
2. After finishing what to do, we commit then push the branch to GitHub, then create a Pull Request.
3. We wait until the automated tests and CI checks are all passed (green), and another person to manually approve it.
4. Another one of us (not the one who worked in that PR) go try and approve the PR if it's valid. Then we merge this into main branch.
5. On Render, i already set both the services's Auto-deploy mode at 'On commit'. With the source branch as the main branch, this means whenever there's something merged into main branch, it will be auto deployed on Render thus available on the public web version.
6. We really go to the public web to test if the newest functions are there.    

We only count a new version as successful once both the deployment of Render and the manual trial done by us on the public web works correctly.

### 1.3. How to go back to the latest good version if something breaks
There are two ways we can do this:
- Via Render's rollback option:
1. Go to Render's dashboard and find the affected service (back or frontend).
2. Trace back the deploy history carefully, there's a history of what deployed.
3. Find the latest good version there (might be found using the same commit code as on GitHub).
4. Choose "Rollback" and confirm. Wait till it's complete.
5. Manually try to verify that the latest good version is brought back.
- Via GitHub's reverse/rollback option:
1. Run this command: git revert <commit-code> and push. Or open GitHub Desktop and check the History tab when being at that repository.
2. Wait for CI green, and wait for approval + merged if needed.
3. Go to Render's dashboard to see if that rollback comit is deployed (if not, it still can be deployed manually).
4. Manually try to verify that the latest good version is brought back.    

Note: This only can be done when we remember the exact commit code of the latest good version, and after all of us have discussed thoroughly on what's the problem and really agree to rollback, as well as notifying again once the rollback is finished to take turns to test manually.

## 2. The CI Pipeline

### 2.1. Overview

The project uses GitHub Actions to automatically verify code changes before they are merged into the `main` branch.

The CI workflow is defined in `.github/workflows/ci.yml`.

The workflow performs the following tasks:
- Checks out the source code.
- Sets up the Python environment.
- Installs project dependencies.
- Checks the MySQL database connection.
- Initializes the test database.
- Runs automated tests using pytest.

The workflow is triggered by the GitHub events configured in `ci.yml`.

### 2.2. CI Workflow Steps

**1. Checkout code**

Uses `actions/checkout@v4` to download the repository source code into the GitHub Actions runner so that subsequent steps can access the project files.

**2. Set up Python**

Uses `actions/setup-python@v5` to configure Python 3.12. It also enables pip dependency caching to reduce installation time in subsequent workflow runs.

**3. Install dependencies**

Upgrades pip and installs the required Python packages from `backend/requirements.txt`.

**4. Check MySQL connection**

Connects to the MySQL test database using the environment variables configured in the workflow. This verifies that the database service is accessible before running the tests.

**5. Initialize test database**

Runs `python -m backend.database.init_db` to initialize the test database and prepare the database schema required by the application.

**6. Run tests**

Runs `python -m pytest tests/ -v` to execute the project's automated test suite and display detailed test results.

### 2.3. CI Execution Evidence

The following information records the actual result of the latest successful CI execution on the `main` branch.

**Latest successful GitHub Actions run:**

![success](images/success1.png)
![success](images/success2.png)

### 2.4. Branch Protection Rules

The `main` branch is protected by GitHub branch protection rules to ensure that code changes are reviewed and verified before merging.

The following requirements are enabled:

1. **Require a pull request before merging:** Direct changes must go through a Pull Request.
2. **Require at least 1 approving review:** At least one reviewer must approve the Pull Request before it can be merged.
3. **Require status checks to pass before merging:** The required CI status check must pass before merging is allowed.

These rules help prevent unreviewed or failing code from being merged into the `main` branch.

 ## 3. Monitoring

**Application Logs**

YUMS is hosted on Render. The team can inspect backend logs through **Render Dashboard → Web Service → Logs** to investigate application errors, failed requests, and database connectivity issues. Passwords, authentication tokens, and sensitive personal information must not be logged.

**Health Check**

- Endpoint: `https://small-shop-tailscale.onrender.com/health`
- HTTP 200: The application and MySQL database are healthy.
- HTTP 503: The health check detects a failure.

**Key Monitoring Metrics**

| Metric | Threshold | Monitoring Method |
|---|---|---|
| Error Rate | 1% | Calculate HTTP 5xx responses as a percentage of total requests when sufficient log data is available. |
| Response Time | 3 seconds (proposed) | Manually measure API request duration using Chrome DevTools → Network → Timing. |

During testing, the deployed `/products` API responded in approximately **2.56 seconds**, including **2.55 seconds waiting for the server response**.

**Incident Detection and Response**

The team uses the `/health` endpoint, Render Logs, and manual response-time checks to investigate application problems. If the error rate exceeds 1% or response times consistently exceed 3 seconds, the team investigates backend errors, database connectivity, and recent deployments.

The Render Free plan limits access to application metrics. Automated threshold-based alerting has not yet been verified.

## 4. Known risks and technical debt
| Item | Layer | What could happen | Plan |
|-------|--------|-------------------------|-------|
| Database based on a specific local Windows laptop only | Infrastructure | Once this machine is turned off or loses internet connection, the backend deployed on Render will lose access to the MySQL database, leading to other people’s device not being able to access the public web. | Improve database availability or find other more sustainable platforms, though might not be free (hire a professional server). |
| API URL configuration | Code | A wrong API such as 127.0.0.1 or else may cause the frontend to fail when accessing the deployed backend. | Centralize API configuration and separate local vs product environments. |
| Database schema synchronization | Data | Missing database columns or schema’s difference between environments may cause SQL errors thus block some features like login from working, | Maintain database migration scripts and keep schemas synchronized. |
| Automated test coverage | Tests | Automated tests written by us are often based on the BR list, so bugs in authentication, product management or other things that aren’t covered in BR may be missed and go undetected. | Add more automated tests for critical features right when spotting something uncovered. |
| Deployment and troubleshooting documentations | Docs | Outdated deploying instructions may cause users to feel puzzled and configure the service wrongly and difficulties when fixing errors. | Review and update the documents regularly, especially after major changes. |

## 5. Maintenance plan
| Area | What to do | Owner | How often |
|-------|---------------|----------|--------------|
Bug fixes | Review bug reports, reproduce issues, handle issues, test the affected features before merging changes | All (backend and frontend developers) | Whenever there’s a bug |
| Dependency updates | Check for outdated dependencies and update them after testing | All (backend and frontend developers) | Monthly |
| Database backups | Make backup version for the MySQL database; verify backup files and regularly test its restoration | Database administrators (oftenly @aizun and @HaVy2006) | Weekly |
Monitoring | Check render deployment status, backend health endpoint, applications logs, and database connectivity | DevOps (mainly @ngocmai141106 at the moment) | Weekly, and ideally after every commit on main |
| Documentation | Review and update setup instructions, API configurations, deployment procedures, rollback instructions etc. | All members | Monthly or after significant changes |

## 6. Lesson learned
*Incorrect API configuration*
What happened: The frontend uses 127.0.0.1:8000 as the API URL. It only works when the backend was running locally, causing the Fail to fetch error when accessing the website.
What we changed: We configured the frontend to use the correct public Render backend URL in production.
What we would do differently next time: Separate development and production environment configurations from the beginning and verify API URLs before deployment.

*Database Schema Inconsistency*
What happened: The backend login function queried the must_change_password column but the MySQL users table didn’t have that column, thus causing the error and returning HTTP 500 error code during login.
What we changed: We added that missing column to the MySQL database while maintaining the existing user records.
What we would do next time: Maintain database migration scripts and test database schema compatibility before deploying backend changes.

*Database connectivity and deployment challenges*
What happened: The deployed backend on Render depends on a MySQL database hosted on a local Windows machine (@ngocmai141106’s) so once the device is turned off, connectivity issues could make the application fail to run even when the backend service is still running.
What we changed: We tried to configure Tailscale, TCP replay and add a health endpoint for the backend to diagnose connection problems. However, this problem is still unsolved and the device above has to stay turned on whenever needed.
What we would do differently next time: Possibly plan infrastructure dependencies earlier and differently, document network configuration and test database connectivity and recovery procedures before deployment.
