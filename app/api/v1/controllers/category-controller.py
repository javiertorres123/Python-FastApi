from services.category_services import CategoryService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate

def get_all_categories_controller(db: Session = Depends(get_db)):
    categories = CategoryService.get_all_categories(db)
    return categories

def get_category_by_id_controller(category_id: int, db: Session = Depends(get_db)):
    category = CategoryService.get_category_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

def create_category_controller(category_data: CategoryCreate, db: Session = Depends(get_db)):
    new_category = CategoryService.create_category(db, category_data)
    return new_category

def update_category_controller(category_id: int, category_data: CategoryUpdate, db: Session = Depends(get_db)):
    existing_category = CategoryService.get_category_by_id(db, category_id)
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")
    updated_category = CategoryService.update_category(db, existing_category, category_data)
    return updated_category

def delete_category_controller(category_id: int, db: Session = Depends(get_db)):
    existing_category = CategoryService.get_category_by_id(db, category_id)
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")
    deleted_category = CategoryService.delete_category(db, existing_category)
    return deleted_category
