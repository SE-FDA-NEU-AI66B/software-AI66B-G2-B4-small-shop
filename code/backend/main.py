import sys
import os
from fastapi import FastAPI, HTTPException, status, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from schema.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from services.employee import add_employee, update_employee, get_all_employees, delete_employee, get_employee_by_id
from schema.order import OrderCreate, CustomerCreate, DeliveryResponse
from services.order import get_products, search_customers, create_customer, create_order, get_orders, get_order_by_id, mark_order_delivered

from config.api import settings

#oanhtran
from schema.product import ProductCreate, ProductUpdate, ProductResponse
from services.product import get_all_products, add_product, update_product, delete_product

from schema.inventory import InventoryCreate, InventoryUpdate, InventoryResponse
from services.inventory import get_all_inventory, add_inventory, update_inventory, delete_inventory

from schema.sales import SalesItemOverview, DemandPredictionResponse, SalesFilterQuery
from services.sales import get_sales_overview, get_demand_predictions
from fastapi import Query
from typing import Optional
#het oanhtran

app = FastAPI(title="YUMS")

# Configure CORS so browser fetch requests (POST, PUT, OPTIONS) are permitted
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from local HTML / frontend servers
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)

emp_router = APIRouter(prefix="/employees", tags=["Employees"])

@emp_router.get(
    "",
    response_model=List[EmployeeResponse],
    summary="Get all employees",
)
def get_all_employees_endpoint():
    """Returns a list of all registered employees."""
    try:
        return get_all_employees()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch employees: {str(e)}",
        )

@emp_router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
    summary="Get employee by ID",
)
def get_employee_by_id_endpoint(employee_id: int):
    """Retrieves a single employee record by ID."""
    employee = get_employee_by_id(employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found.",
        )
    return employee
    
@emp_router.post(
    "",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new employee",
)
def create_employee_endpoint(payload: EmployeeCreate):
    try:
        new_employee = add_employee(payload)
        return new_employee
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create employee: {str(e)}",
        )


@emp_router.put(
    "/{employee_id}",
    response_model=EmployeeResponse,
    summary="Update employee details",
)
def update_employee_endpoint(employee_id: int, payload: EmployeeUpdate):
    updated_employee = update_employee(employee_id, payload)
    if not updated_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found.",
        )
    return updated_employee

@emp_router.delete("/{employee_id}", status_code=status.HTTP_200_OK)
def delete_employee_endpoint(employee_id: int):
    return delete_employee(employee_id=employee_id)

app.include_router(emp_router)

#all routers for order screns of maitran
api_router = APIRouter(prefix="/api")

@api_router.get("/products", tags=["Products"])
def get_products_endpoint():
    return get_products()

@api_router.post("/orders", tags=["Orders"], status_code=status.HTTP_201_CREATED)
def create_order_endpoint(payload: OrderCreate):
    return create_order(payload)

@api_router.get("/orders", tags=["Orders"])
def get_orders_endpoint():
    return get_orders()

@api_router.get("/orders/{order_id}", tags=["Orders"])
def get_order_endpoint(order_id: int):
    order = get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found.")
    return order

@api_router.patch("/orders/{order_id}/deliver", response_model=DeliveryResponse, tags=["Orders"])
def deliver_order_endpoint(order_id: int):
    return mark_order_delivered(order_id)

#2 customer endpoints since maitran need them for the create ord screen
@api_router.get("/customers/search", tags=["Customers"])
def search_customers_endpoint(phone: str = ""):
    return search_customers(phone)

@api_router.post("/customers", tags=["Customers"], status_code=status.HTTP_201_CREATED)
def create_customer_endpoint(payload: CustomerCreate):
    return create_customer(payload)

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",  # Pass as string when reload=True
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD
    )

# oanhtran: product endpoints

@app.get("/products", response_model=List[ProductResponse], summary="Get all products")
def get_all_products_endpoint():
    try:
        return get_all_products()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch products: {str(e)}")

@app.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED, summary="Add a new product")
def create_product_endpoint(payload: ProductCreate):
    try:
        return add_product(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create product: {str(e)}")

@app.put("/products/{product_id}", response_model=ProductResponse, summary="Update product details")
def update_product_endpoint(product_id: int, payload: ProductUpdate):
    updated = update_product(product_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found.")
    return updated

@app.delete("/products/{product_id}", summary="Delete a product")
def delete_product_endpoint(product_id: int):
    success = delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found.")
    return {"message": f"Product {product_id} deleted successfully."}

# oanhtran: inventory endpoints

@app.get("/inventory", response_model=List[InventoryResponse], summary="Get all inventory products")
def get_all_inventory_endpoint():
    try:
        return get_all_inventory()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch inventory: {str(e)}")

@app.post("/inventory", response_model=InventoryResponse, status_code=status.HTTP_201_CREATED, summary="Add a new inventory product")
def create_inventory_endpoint(payload: InventoryCreate):
    try:
        return add_inventory(payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create item: {str(e)}")

@app.put("/inventory/{sku}", response_model=InventoryResponse, summary="Update inventory product")
def update_inventory_endpoint(sku: str, payload: InventoryUpdate):
    updated = update_inventory(sku, payload)
    if not updated:
        raise HTTPException(status_code=404, detail=f"Product SKU {sku} not found.")
    return updated

@app.delete("/inventory/{sku}", summary="Delete inventory product")
def delete_inventory_endpoint(sku: str):
    if not delete_inventory(sku):
        raise HTTPException(status_code=404, detail=f"Product SKU {sku} not found.")
    return {"message": f"Product {sku} deleted successfully."}


# oanhtran: sales endpoints and analytics

@app.get("/sales/overview", summary="Get sales overview (US11)")
def get_sales_overview_endpoint(
    top_n: Optional[str] = Query("5"),
    category: Optional[str] = Query(None),
    timeframe: Optional[str] = Query("monthly")
):
    try:
        from services.sales import get_sales_overview
        return get_sales_overview(top_n=top_n, category=category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch sales overview: {str(e)}")

@app.get("/sales/predictions", summary="Get demand forecasting (US15, US16)")
def get_demand_predictions_endpoint(window_days: int = Query(30)):
    try:
        from services.sales import get_demand_predictions
        return get_demand_predictions(window_days=window_days)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to calculate predictions: {str(e)}")