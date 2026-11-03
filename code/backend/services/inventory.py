import os
import sys
from typing import Optional, List, Dict, Any

# Đảm bảo thêm thư mục gốc vào sys.path để gọi được database
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.connect_db import get_connection
from schema.inventory import InventoryCreate, InventoryUpdate

def get_all_inventory() -> List[Dict[str, Any]]:
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            query = """
                SELECT 
                    p.product_id,
                    p.name AS product_name,
                    p.category_id,
                    COALESCE(c.category_name, 'General') AS category_name,
                    p.unit_price,
                    100 AS stock_quantity,
                    '2026-10-01' AS import_date,
                    'In Stock' AS status,
                    'bg-success' AS badge_class,
                    CONCAT('P-', LPAD(p.product_id, 3, '0')) AS sku
                FROM products p
                LEFT JOIN categories c ON p.category_id = c.category_id
                ORDER BY p.product_id DESC;
            """
            cursor.execute(query)
            return cursor.fetchall() or []
    finally:
        connection.close()

def add_inventory(item_data: InventoryCreate) -> Dict[str, Any]:
    connection = get_connection()
    try:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(
                "INSERT INTO products (name, category_id, unit_price, is_available) VALUES (%s, %s, %s, %s)",
                (item_data.product_name, item_data.category_id, item_data.unit_price, True)
            )
            product_id = cursor.lastrowid
            cursor.execute("""
                SELECT p.product_id, p.name AS product_name, p.category_id, 
                       COALESCE(c.category_name, 'General') AS category_name,
                       p.unit_price, 100 AS stock_quantity, '2026-10-01' AS import_date,
                       'In Stock' AS status, 'bg-success' AS badge_class,
                       CONCAT('P-', LPAD(p.product_id, 3, '0')) AS sku
                FROM products p
                LEFT JOIN categories c ON p.category_id = c.category_id
                WHERE p.product_id = %s
            """, (product_id,))
            return cursor.fetchone()
    finally:
        connection.close()

def update_inventory(sku: str, item_data: InventoryUpdate) -> Optional[Dict[str, Any]]:
    connection = get_connection()
    try:
        product_id = int(sku.replace("P-", ""))
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(
                "UPDATE products SET name = %s, unit_price = %s WHERE product_id = %s",
                (item_data.product_name, item_data.unit_price, product_id)
            )
            cursor.execute("""
                SELECT p.product_id, p.name AS product_name, p.category_id, 
                       COALESCE(c.category_name, 'General') AS category_name,
                       p.unit_price, 100 AS stock_quantity, '2026-10-01' AS import_date,
                       'In Stock' AS status, 'bg-success' AS badge_class,
                       CONCAT('P-', LPAD(p.product_id, 3, '0')) AS sku
                FROM products p
                LEFT JOIN categories c ON p.category_id = c.category_id
                WHERE p.product_id = %s
            """, (product_id,))
            return cursor.fetchone()
    finally:
        connection.close()

def delete_inventory(sku: str) -> bool:
    connection = get_connection()
    try:
        product_id = int(sku.replace("P-", ""))
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("DELETE FROM products WHERE product_id = %s;", (product_id,))
            return cursor.rowcount > 0
    finally:
        connection.close()