from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length= 100, example="Electronics")
    description: str = Field(..., example="Devices and gadgets")
    status: bool = Field(..., example=True)
    products: list = Field(default=[], example=[]) 

class CategoryCreate(CategoryBase):
    name: str = Field(..., min_length=3, max_length= 100, example="Electronics")
    description: str = Field(..., example="Devices and gadgets")

class CategoryUpdate(CategoryBase):
    name: str = Field(..., min_length=3, max_length= 100, example="Electronics")
    description: str = Field(..., example="Devices and gadgets")
    status: bool = Field(..., example=True)

