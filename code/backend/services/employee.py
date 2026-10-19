import os
import sys
from fastapi import HTTPException, status
from typing import Optional, Dict, Any
import pymysql
from typing import List, Dict, Any

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from backend.database.connect_db import get_connection
from backend.schema.employee import EmployeeCreate, EmployeeUpdate

def get_all_employees() -> List[Dict[str, Any]]:
    """Retrieves all employee records from the database ordered by ID descending."""
    connection = get_connection()
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection failed."
        )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employees ORDER BY employee_id DESC;")
            employees = cursor.fetchall()
            return employees if employees else []
    finally:
        connection.close()

def add_employee(employee_data: EmployeeCreate) -> Dict[str, Any]:
    """Inserts a new employee into the database and returns the inserted record.
    Prevents creation if an exact duplicate record already exists across all fields.
    """
    connection = get_connection()
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection failed."
        )
    
    try:
        with connection.cursor() as cursor:
            # 1. Check for exact duplicate across ALL incoming fields
            check_query = """
                SELECT employee_id FROM employees 
                WHERE name <=> %s 
                  AND email <=> %s 
                  AND phone <=> %s 
                  AND role <=> %s 
                  AND status <=> %s;
            """
            cursor.execute(
                check_query,
                (
                    employee_data.name,
                    employee_data.email,
                    employee_data.phone,
                    employee_data.role,
                    employee_data.status,
                )
            )
            
            existing_employee = cursor.fetchone()
            if existing_employee:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="An identical employee record with these exact details already exists."
                )

            # 2. Insert new record if no duplicate exists
            insert_query = """
                INSERT INTO employees (name, email, phone, role, status)
                VALUES (%s, %s, %s, %s, %s);
            """
            cursor.execute(
                insert_query,
                (
                    employee_data.name,
                    employee_data.email,
                    employee_data.phone,
                    employee_data.role,
                    employee_data.status,
                ),
            )
            connection.commit()
            employee_id = cursor.lastrowid

            # 3. Fetch newly created employee record
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
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection failed."
        )
    
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
    if not connection:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection failed."
        )
    
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employees WHERE employee_id = %s;", (employee_id,))
            return cursor.fetchone()
    finally:
        connection.close()


def delete_employee(employee_id: int) -> Dict[str, str]:
    pass