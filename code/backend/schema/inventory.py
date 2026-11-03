from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class InventoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    category_id: Optional[int] = Field(None, description="ID danh mục từ bảng category")
    unit_price: float = Field(..., ge=0, description="Giá sản phẩm (VND)")
    stock: int = Field(50, ge=0)
    min_stock: int = Field(10, ge=0)
    image: Optional[str] = Field(None, max_length=255)

class InventoryCreate(InventoryBase):
    sku: Optional[str] = Field(None, max_length=20)

class InventoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    category_id: Optional[int] = None
    unit_price: Optional[float] = Field(None, ge=0)
    stock: Optional[int] = Field(None, ge=0)
    min_stock: Optional[int] = Field(None, ge=0)
    image: Optional[str] = Field(None, max_length=255)

class InventoryResponse(BaseModel):
    product_id: int
    sku: str
    name: str
    category_id: Optional[int] = None
    category_name: Optional[str] = None
    unit_price: float
    stock: int
    min_stock: int
    image: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)