import os
import sys
from typing import Optional, List, Dict, Any

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from backend.database.connect_db import get_connection
from backend.schema.inventory import InventoryCreate, InventoryUpdate

def get_all_inventory() -> List[Dict[str, Any]]:
    """Lấy danh sách tất cả sản phẩm kèm LEFT JOIN với bảng category để lấy đúng tên danh mục."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT p.product_id, p.name, p.category_id, c.category_name, p.unit_price, p.is_available,
                       CONCAT('P-', LPAD(p.product_id, 3, '0')) AS sku,
                       50 AS stock, 10 AS min_stock
                FROM product p
                LEFT JOIN category c ON p.category_id = c.category_id
                ORDER BY p.product_id DESC;
            """
            cursor.execute(query)
            products = cursor.fetchall()
            return products if products else []
    finally:
        connection.close()

def get_inventory_by_sku(sku: str) -> Optional[Dict[str, Any]]:
    """Lấy thông tin sản phẩm theo SKU."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            product_id = int(sku.replace('P-', '').replace('p-', ''))
            query = """
                SELECT p.product_id, p.name, p.category_id, c.category_name, p.unit_price, p.is_available,
                       CONCAT('P-', LPAD(p.product_id, 3, '0')) AS sku,
                       50 AS stock, 10 AS min_stock
                FROM product p
                LEFT JOIN category c ON p.category_id = c.category_id
                WHERE p.product_id = %s;
            """
            cursor.execute(query, (product_id,))
            return cursor.fetchone()
    except Exception:
        return None
    finally:
        connection.close()

def add_inventory(item_data: InventoryCreate) -> Dict[str, Any]:
    """Thêm sản phẩm mới vào bảng product."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO product (name, category_id, unit_price, is_available)
                VALUES (%s, %s, %s, %s);
            """
            cat_id = getattr(item_data, 'category_id', 1) or 1
            price_val = getattr(item_data, 'unit_price', getattr(item_data, 'price', 0))
            
            cursor.execute(query, (item_data.name, cat_id, price_val, True))
            product_id = cursor.lastrowid

            cursor.execute("""
                SELECT p.product_id, p.name, p.category_id, c.category_name, p.unit_price, p.is_available,
                       CONCAT('P-', LPAD(p.product_id, 3, '0')) AS sku,
                       50 AS stock, 10 AS min_stock
                FROM product p
                LEFT JOIN category c ON p.category_id = c.category_id
                WHERE p.product_id = %s;
            """, (product_id,))
            return cursor.fetchone()
    finally:
        connection.close()

def update_inventory(sku: str, item_data: InventoryUpdate) -> Optional[Dict[str, Any]]:
    """Cập nhật thông tin sản phẩm trong database."""
    try:
        product_id = int(sku.replace('P-', '').replace('p-', ''))
    except Exception:
        return None

    update_data = item_data.model_dump(exclude_unset=True)
    if not update_data:
        return get_inventory_by_sku(sku)

    if 'price' in update_data:
        update_data['unit_price'] = update_data.pop('price')

    set_clause = ", ".join([f"`{key}` = %s" for key in update_data.keys()])
    values = list(update_data.values()) + [product_id]

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = f"UPDATE product SET {set_clause} WHERE product_id = %s;"
            cursor.execute(query, values)

            cursor.execute("""
                SELECT p.product_id, p.name, p.category_id, c.category_name, p.unit_price, p.is_available,
                       CONCAT('P-', LPAD(p.product_id, 3, '0')) AS sku,
                       50 AS stock, 10 AS min_stock
                FROM product p
                LEFT JOIN category c ON p.category_id = c.category_id
                WHERE p.product_id = %s;
            """, (product_id,))
            return cursor.fetchone()
    finally:
        connection.close()

def delete_inventory(sku: str) -> bool:
    """Xóa sản phẩm theo SKU."""
    try:
        product_id = int(sku.replace('P-', '').replace('p-', ''))
    except Exception:
        return False

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM product WHERE product_id = %s;", (product_id,))
            return cursor.rowcount > 0
    finally:
        connection.close()