from app.services.product_services import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db

def get_all_products_controller(db: Session = Depends(get_db)):
    products = get_all_products(db)
    return products

def get_product_by_id_controller(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def create_product_controller(product_data: ProductCreate, db: Session = Depends(get_db)):
    new_product = create_product(db, product_data)
    return new_product

def update_product_controller(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    existing_product = get_product_by_id(db, product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product = update_product(db, existing_product, product_data)
    return updated_product

def delete_product_controller(product_id: int, db: Session = Depends(get_db)):
    existing_product = get_product_by_id(db, product_id)
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    deleted_product = delete_product(db, existing_product)
    return deleted_product