from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length= 100, example="Electronics")
    description: str = Field(..., example="Devices and gadgets")

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: str = Field(..., min_length=3, max_length= 100, example="Electronics")
    description: str = Field(..., example="Devices and gadgets")
    status: bool = Field(..., example=True)

