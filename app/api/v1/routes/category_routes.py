from fastapi import APIRouter
from sqlalchemy.orm import Session, Depends
from app.core.database import get_db
from app.api.v1.controllers.category_controller import get_all_categories_controller, get_category_by_id_controller, create_category_controller, update_category_controller, delete_category_controller

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/get-all")
def get_all_categories(db: Session = Depends(get_db)):
    return get_all_categories_controller(db)

@router.get("/{category_id}")
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return get_category_by_id_controller(category_id, db)

@router.post("/create")
def create_category(data, db: Session = Depends(get_db)): 
    return create_category_controller(data, db)

@router.put("/update/{category_id}")
def update_category(category_id: int, db: Session = Depends(get_db)):
    return update_category_controller(category_id, db)

@router.delete("/delete/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return delete_category_controller(category_id, db)

