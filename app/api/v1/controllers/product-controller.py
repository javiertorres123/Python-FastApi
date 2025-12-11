from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.product import ProductCreate, ProductUpdate
from app.models.product import Product
from app.services.product_services import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product
)

def get_all_products_controller(db: Session = Depends(get_db)):
    return get_all_products(db)


def get_product_by_id_controller(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def create_product_controller(product_data: ProductCreate, db: Session = Depends(get_db)):
    # ✔ Convertimos el schema a un modelo SQLAlchemy
    new_product = Product(**product_data.dict())
    return create_product(db, new_product)


def update_product_controller(product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # ✔ Aplicar cambios del schema al modelo
    update_data = product_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(product, key, value)

    return update_product(db, product)


def delete_product_controller(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return delete_product(db, product)
