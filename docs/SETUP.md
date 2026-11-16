# YUMS – Setup and Installation Guide

This document explains how to set up and run **YUMS (YoU Manage your Shop)** locally or in GitHub Codespaces. It also includes instructions for database initialization, frontend access, test execution, and troubleshooting.

## 1. Prerequisites

Install or prepare the following tools:

| Tool | Recommended version | Purpose |
|---|---|---|
| Python | 3.12 | Backend and test execution |
| MySQL | 8.0 | Application database |
| Git | Latest | Clone and manage the repository |
| Docker | Latest | Run MySQL in Codespaces or locally (optional) |
| Visual Studio Code | Latest | Recommended development environment |

> **Note:** Use Python 3.12 to match the project's GitHub Actions CI environment.

## 2. Get the Source Code

Clone the repository:

```bash
git clone https://github.com/SE-FDA-NEU-AI66B/software-AI66B-G2-B4-small-shop.git
```

Move into the project directory:

```bash
cd software-AI66B-G2-B4-small-shop/code
```

All subsequent terminal commands in this guide assume that the current directory is `code/`, unless stated otherwise.

## 3. Set Up the Python Environment

### 3.1. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux, macOS, or GitHub Codespaces:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If your environment uses `python` instead of `python3`, you can use:

```bash
python -m venv .venv
```

After activation, install the project dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

Check the Python version:

```bash
python --version
```

Make sure Python 3.12 is being used.

## 4. Configure the MySQL Database

YUMS requires a running MySQL database. Choose **one** of the following options.

### Option A: Use an Existing MySQL Server

If MySQL is already installed on your machine:

1. Start the MySQL service.
2. Log in to MySQL.
3. Create the application database if it does not already exist:

```sql
CREATE DATABASE mini_shop;
```

4. Keep your MySQL username and password available for the next configuration step.

### Option B: Run MySQL with Docker

This option is recommended for GitHub Codespaces or environments without a local MySQL installation.

Start a MySQL 8.0 container:

```bash
docker run --name yums-mysql \
  -e MYSQL_ROOT_PASSWORD=root12345 \
  -e MYSQL_DATABASE=mini_shop \
  -p 3306:3306 \
  -d mysql:8.0
```

Wait for MySQL to become ready:

```bash
docker logs -f yums-mysql
```

Wait until the logs indicate that MySQL is ready for connections. Press `Ctrl + C` to exit the log view. The container will continue running.

**If the container already exists**, do not run the creation command again. Check its status:

```bash
docker ps -a
```

Start the existing container if it is stopped:

```bash
docker start yums-mysql
```

Check its logs:

```bash
docker logs yums-mysql
```

> **Important:** `root12345` is a development password used in this example. The password in your application configuration must match the password configured when the MySQL container was created. Changing `.env` does not change the MySQL account password.

## 5. Configure Environment Variables

Create a `.env` file inside the `backend/` directory.

The expected path is:

```text
code/
└── backend/
    └── .env
```

If the project provides `backend/.env.example`, copy it first:

**Windows (PowerShell):**

```powershell
Copy-Item backend/.env.example backend/.env
```

**Linux, macOS, or Codespaces:**

```bash
cp backend/.env.example backend/.env
```

If the example file is unavailable, create `backend/.env` manually.

Configure the database variables:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=root12345
DB_NAME=mini_shop
```

Adjust these values according to your MySQL configuration.

- `DB_HOST`: MySQL server address.
- `DB_PORT`: MySQL server port.
- `DB_USER`: MySQL username.
- `DB_PASSWORD`: MySQL password.
- `DB_NAME`: Application database name.

Also configure the JWT secret required by the application. If the project uses `JWT_SECRET_KEY`, generate a secure value with:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Copy the generated value into `backend/.env`:

```env
JWT_SECRET_KEY=your_generated_secret
```

Use the variable names expected by `backend/.env.example` and the application. Do not commit `.env` or expose real credentials in GitHub.

## 6. Initialize the Database

Make sure:

- Your virtual environment is activated.
- MySQL is running.
- The database configuration in `backend/.env` is correct.
- The `mini_shop` database exists.

From the `code/` directory, run:

```bash
python -m backend.database.init_db
```

This initializes the database tables required by the application.

If initialization fails, check the MySQL connection and environment variables before proceeding.

## 7. Run the Backend

From the `code/` directory, start the backend:

```bash
python backend/main.py
```

If the application starts successfully, keep the terminal running.

For GitHub Codespaces, open the **Ports** tab and make the backend port accessible if required. Use the port displayed by the application startup output.

## 8. Run the Frontend

The frontend is located in:

```text
code/frontend/index.html
```

You can open it using either of these methods:

**Option A: Visual Studio Code Live Server**

1. Open the project in Visual Studio Code.
2. Open `frontend/index.html`.
3. Right-click the file.
4. Select **Open with Live Server**.

**Option B: Python HTTP Server**

From the `code/` directory, run:

```bash
python -m http.server 5500 --directory frontend
```

Then open:

```text
http://localhost:5500
```

For GitHub Codespaces, open port `5500` from the **Ports** tab.

> Make sure the frontend is configured to communicate with the correct backend URL. In Codespaces, use the forwarded backend URL when accessing the application remotely.

## 9. Demo Accounts

The following accounts are provided for application testing:

| Username | Password | Role |
|---|---|---|
| `havy` | `12345` | Admin |
| `minhanh` | `minhanh` | Employee |

The application provides role-based access:

- **Admin:** Can access management functions and administrative features.
- **Employee:** Has access to permitted employee operations.

These are demo credentials. Do not use them as production credentials.

## 10. Run All Test Cases

Run tests from the `code/` directory with the virtual environment activated.

First, ensure dependencies are installed:

```bash
python -m pip install -r backend/requirements.txt
```

Then execute the complete test suite:

```bash
python -m pytest tests/ -v
```

This command discovers and runs all test files under `tests/`, rather than running only sales-related tests.

Useful alternatives:

**Show print output during test execution:**

```bash
python -m pytest tests/ -v -s
```

**Generate a coverage report:**

Install the optional coverage package:

```bash
python -m pip install pytest-cov
```

Run:

```bash
python -m pytest tests/ --cov=backend --cov-report=term-missing
```

> **Note:** Tests that access MySQL require a running database and valid environment configuration. If a test fails, check the error output to determine whether it is caused by the application, test data, dependencies, or database connection.

## 11. GitHub Codespaces Quick Setup

For a fresh GitHub Codespace, follow this sequence:

1. Open the repository on GitHub.
2. Select **Code → Codespaces → Create codespace**.
3. Open the terminal and enter the project directory:

```bash
cd code
```

4. Create and activate the Python environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

5. Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r backend/requirements.txt
```

6. Start MySQL using the Docker instructions in [Section 4](#4-configure-the-mysql-database).

7. Create and configure `backend/.env` using [Section 5](#5-configure-environment-variables).

8. Initialize the database:

```bash
python -m backend.database.init_db
```

9. Start the backend:

```bash
python backend/main.py
```

10. Open the backend port from the Codespaces **Ports** tab. In another terminal, start the frontend using the instructions in [Section 8](#8-run-the-frontend).

11. Run the test suite:

```bash
python -m pytest tests/ -v
```

## 12. Troubleshooting

### MySQL connection refused

Example:

```text
Connection refused
```

Possible causes:

- MySQL is not running.
- The MySQL container has stopped.
- The configured host or port is incorrect.

Check the Docker container:

```bash
docker ps -a
```

If it is stopped:

```bash
docker start yums-mysql
```

Check that MySQL is ready:

```bash
docker logs yums-mysql
```

### MySQL access denied

Example:

```text
Access denied for user 'root'
```

Possible causes:

- The username or password in `backend/.env` is incorrect.
- The password configured in `.env` does not match the existing MySQL account.
- The container was created previously with a different password.

Check the credentials used when the MySQL container was first created. Updating `.env` alone does not reset the database password.

### Missing Python package

Example:

```text
ModuleNotFoundError: No module named 'jwt'
```

Activate the virtual environment and reinstall dependencies:

```bash
python -m pip install -r backend/requirements.txt
```

If the package is still missing, check that the required dependency is declared in `backend/requirements.txt`.

### Database initialization fails

Check that:

- MySQL is running and ready.
- The database `mini_shop` exists.
- The database credentials in `backend/.env` are correct.
- The command is executed from the `code/` directory.

### Backend does not start

Check that:

- The virtual environment is activated.
- All required dependencies are installed.
- `backend/.env` exists and contains valid configuration.
- MySQL is running and accessible.

Review the terminal output for the specific error.

### Tests fail

Run the test suite with detailed output:

```bash
python -m pytest tests/ -v -s
```

Check the failure message, database state, environment variables, and installed dependencies. Make sure the test database is initialized before running tests that require it.

## 13. Online Deployment

The deployed YUMS application is available at:

**Frontend:** [YUMS Application](https://yums-frontend-qjq2.onrender.com)

The online application uses its deployed backend and database configuration. Local setup instructions in this document are intended for development and testing.