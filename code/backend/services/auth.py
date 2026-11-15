import os
import secrets
import sys
import threading
import time
from typing import Any, Dict

import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from backend.database.connect_db import get_connection


def hash_password(password: str) -> str:
    """Hash a plaintext password before storing it for account creation or updates."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("ascii")

def authenticate_user(username: str, password: str) -> Dict[str, Any]:
    """Authenticate an exact username/password pair and return non-sensitive user data."""
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT user_id, username, password, role, is_active,
                       must_change_password
                FROM users
                WHERE BINARY username = BINARY %s;
                """,
                (username,),
            )
            user = cursor.fetchone()

        password_matches = False
        if user:
            try:
                password_matches = bcrypt.checkpw(
                    password.encode("utf-8"),
                    user["password"].encode("ascii"),
                )
            except (TypeError, ValueError, UnicodeError):
                password_matches = False

        if not user or not password_matches or not user["is_active"]:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password.",
            )

        return {
            "user_id": user["user_id"],
            "username": user["username"],
            "role": user["role"],
            "must_change_password": bool(user["must_change_password"]),
            #"access_token": _create_session(user["user_id"]),
        }
    finally:
        connection.close()


def change_password(user_id: int, new_password: str) -> None:
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT password FROM users WHERE user_id = %s AND is_active = TRUE",
                (user_id,),
            )
            user = cursor.fetchone()
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User account is unavailable. Please sign in again.",
                )
            if bcrypt.checkpw(
                new_password.encode("utf-8"),
                user["password"].encode("ascii"),
            ):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Choose a password different from your current password.",
                )
            cursor.execute(
                """
                UPDATE users
                SET password = %s, must_change_password = FALSE
                WHERE user_id = %s
                """,
                (hash_password(new_password), user_id),
            )
            connection.commit()
    except HTTPException:
        connection.rollback()
        raise
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()