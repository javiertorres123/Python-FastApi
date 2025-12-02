from fastapi import FastAPI

app = FastAPI(title="Sistema de Inventario")

@app.get("/Products/get-all")
def get_all_products():
    return {"message": "Lista de productos"}

@app.get("/Products/{product_id}")
def get_product_by_id(product_id: int):
    return {"message": f"Detalles del producto {product_id}"}

@app.post("/Products/create")
def create_product():
    return {"message": "Producto creado"}

@app.put("/Products/update/{product_id}")
def update_product(product_id: int):
    return {"message": f"Producto {product_id} actualizado"}

@app.delete("/Products/delete/{product_id}")
def delete_product(product_id: int):
    return {"message": f"Producto {product_id} eliminado"}


