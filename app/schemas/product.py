from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(..., example="Laptop")
    description: str = Field(..., example="A high-performance laptop")
    price_buy: float = Field(..., example=999.99)
    price_sale: float = Field(..., example=1299.99)
    stock: int = Field(..., example=5)
    id_category: int = Field(..., example=1)


class ProductCreate(ProductBase):
    stock: int = Field(..., example=10)

class ProductUpdate(BaseModel):
   name: str = Field(..., example="Laptop")
   description: str = Field(..., example="An updated description for the laptop")
   price_buy: float = Field(..., example=899.99)
   price_sale: float = Field(..., example=1199.99)
   stock: int = Field(..., example=8)
   id_category: int = Field(..., example=2)
   status: bool = Field(..., example=True)

class ProductResponse(ProductBase):
    id: int
    stock: int
    status: bool
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True
