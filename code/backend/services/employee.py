import os
import sys
from typing import Optional, Dict, Any
import pymysql

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from backend.database.connect_db import get_connection
from backend.schema.employee import EmployeeCreate, EmployeeUpdate


def add_employee(employee_data: EmployeeCreate) -> Dict[str, Any]:
    """Inserts a new employee into the database and returns the inserted record."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO employees (name, email, phone, role, status)
                VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(
                query,
                (
                    employee_data.name,
                    employee_data.email,
                    employee_data.phone,
                    employee_data.role,
                    employee_data.status,
                ),
            )
            employee_id = cursor.lastrowid

            # Fetch created employee record
            cursor.execute("SELECT * FROM employees WHERE employee_id = %s;", (employee_id,))
            new_employee = cursor.fetchone()
            return new_employee
    finally:
        connection.close()


def update_employee(employee_id: int, employee_data: EmployeeUpdate) -> Optional[Dict[str, Any]]:
    """Updates non-null fields of an existing employee and returns the updated record."""
    # Exclude unset fields from the payload
    update_data = employee_data.model_dump(exclude_unset=True)
    if not update_data:
        # Return current state if nothing was passed
        return get_employee_by_id(employee_id)

    # Build SET clause dynamically (e.g. "full_name = %s, salary = %s")
    set_clause = ", ".join([f"`{key}` = %s" for key in update_data.keys()])
    values = list(update_data.values())
    values.append(employee_id)

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = f"UPDATE employees SET {set_clause} WHERE employee_id = %s;"
            cursor.execute(query, values)

            if cursor.rowcount == 0:
                # Check if employee exists
                cursor.execute("SELECT 1 FROM employees WHERE employee_id = %s;", (employee_id,))
                if not cursor.fetchone():
                    return None

            cursor.execute("SELECT * FROM employees WHERE employee_id = %s;", (employee_id,))
            return cursor.fetchone()
    finally:
        connection.close()


def get_employee_by_id(employee_id: int) -> Optional[Dict[str, Any]]:
    """Helper to fetch an employee by ID."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employees WHERE employee_id = %s;", (employee_id,))
            return cursor.fetchone()
    finally:
        connection.close()