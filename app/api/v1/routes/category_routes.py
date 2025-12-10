from fastapi import APIRouter

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.get("/get-all")
def get_all_categories():
    return {"message": "Lista de categorías"}

@router.get("/{category_id}")
def get_category_by_id(category_id: int):
    return {"message": f"Detalles de la categoría {category_id}"}

@router.post("/create")
def create_category(): 
    return {"message": "Categoría creada"}

@router.put("/update/{category_id}")
def update_category(category_id: int):
    return {"message": f"Categoría {category_id} actualizada"}

@router.delete("/delete/{category_id}")
def delete_category(category_id: int):
    return {"message": f"Categoría {category_id} eliminada"}

