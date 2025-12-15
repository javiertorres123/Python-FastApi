from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.v1.controllers.product_controller import (
    get_all_products_controller,
    get_product_by_id_controller,
    create_product_controller,
    update_product_controller,
    delete_product_controller,
    calculate_margin_controller
)  
from app.schemas.product import ProductCreate, ProductUpdate

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/get-all")
def get_all_products(db: Session = Depends(get_db)):
    return get_all_products_controller(db)

@router.get("/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_id_controller(product_id, db)
    
@router.post("/create")
def create_product(db: Session = Depends(get_db), product_data: ProductCreate = Depends()):
    return create_product_controller(product_data, db)

@router.put("/update/{product_id}")
def update_product(product_id: int, db: Session = Depends(get_db), product_data: ProductUpdate = Depends()):
    return update_product_controller(product_id, product_data, db)

@router.delete("/delete/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product_controller(product_id, db)

@router.get("/margin/{product_id}")
def calculate_margin(product_id: int, db: Session = Depends(get_db)):
    return calculate_margin_controller(product_id, db)

