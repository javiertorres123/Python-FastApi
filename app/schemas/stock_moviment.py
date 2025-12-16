from pydantic import BaseModel, Field

class StockMovimentBase(BaseModel):
    product_id: int = Field(..., example=1)
    quantity: int = Field(..., example=10)
    moviment_type: str = Field(..., example="IN")  
    reason: str = Field(None, example="Restocking")
    stock_after: int = Field(..., example=50)
    status: bool = Field(..., example=True)

class StockMovimentCreate(StockMovimentBase):
    pass

class StockMovimentResponse(StockMovimentBase):
    id: int
    created_at: str

    class Config:
        from_attributes = True

class StockMovimentUpdate(BaseModel):
    quantity: int = Field(..., example=15)
    moviment_type: str = Field(..., example="OUT")  
    reason: str = Field(None, example="Customer return")
    stock_after: int = Field(..., example=35)
    status: bool = Field(..., example=True)


