from typing import List, Dict, Any
from fastapi import HTTPException, status

from database.connect_db import get_connection


def get_all_customers() -> List[Dict[str, Any]]:
    """Retrieve all customers with their membership names."""

    connection = get_connection()

    if not connection:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection failed."
        )

    try:
        with connection.cursor() as cursor:
            query = """
                SELECT
                    c.customer_id,
                    c.name,
                    c.phone,
                    c.email,
                    c.total_spent,
                    ct.type_name AS membership,
                    c.created_at
                FROM customers AS c
                LEFT JOIN customer_types AS ct
                    ON c.customer_type_id = ct.customer_type_id
                ORDER BY c.customer_id DESC;
            """

            cursor.execute(query)
            customers = cursor.fetchall()

            return customers if customers else []

    finally:
        connection.close()