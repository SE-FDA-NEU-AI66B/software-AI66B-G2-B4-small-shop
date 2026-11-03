import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "backend"))
sys.path.insert(0, BACKEND_DIR)

import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

# US11: SALES ANALYTICS 

def test_tc_us11_01_get_sales_overview_normal():
    """TC-US11-01: Normal case - Get Top 5 Beverage items"""
    response = client.get("/sales/overview?top_n=5&category=Beverage")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 5

def test_tc_us11_02_invalid_top_n_format():
    """TC-US11-02: Error case - Invalid parameter type for top_n"""
    response = client.get("/sales/overview?top_n=invalid_text")
    assert response.status_code in [400, 422, 500]

def test_tc_us11_03_top_n_boundary_limit_one():
    """TC-US11-03: Boundary case - Top N = 1 (Lower valid bound)"""
    response = client.get("/sales/overview?top_n=1")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1

def test_tc_us11_04_top_n_boundary_below_zero():
    """TC-US11-04: Boundary case - Top N = 0 (Below valid bound)"""
    response = client.get("/sales/overview?top_n=0")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 0

