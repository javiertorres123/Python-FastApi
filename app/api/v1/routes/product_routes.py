from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/get-all")
def get_all_products():
    return {"message": "Lista de productos"}

@router.get("/{product_id}")
def get_product_by_id(product_id: int):
    return {"message": f"Detalles del producto {product_id}"}

@router.post("/create")
def create_product():
    return {"message": "Producto creado"}

@router.put("/update/{product_id}")
def update_product(product_id: int):
    return {"message": f"Producto {product_id} actualizado"}

@router.delete("/delete/{product_id}")
def delete_product(product_id: int):
    return {"message": f"Producto {product_id} eliminado"}
