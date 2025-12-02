from api.v1.routes.product_routes import router as product_router
from fastapi import FastAPI

def include_router(product_router, prefix = "/api/v1/products"):
    app = FastAPI()
    app.include_router(product_router, prefix=prefix)
    return app