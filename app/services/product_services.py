from app.models.product import Product
from app.models.category import Category
from app.schemas.product import ProductCreate, ProductUpdate


# 📌 Listar solo productos activos (por defecto)
def get_all_products(db):
    return db.query(Product).filter(Product.status == True).all()


def get_product_by_id(db, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


# 📌 Crear producto con reglas de negocio
def create_product(db, product_data: ProductCreate):

    # Validar categoría existente
    category = db.query(Category).filter(Category.id == product_data.id_category).first()
    if not category:
        raise ValueError("La categoría no existe")

    # Validaciones de negocio
    if product_data.stock < 0:
        raise ValueError("El stock no puede ser negativo")

    if product_data.price_buy < 0 or product_data.price_sale < 0:
        raise ValueError("Los precios no pueden ser negativos")

    if product_data.price_sale < product_data.price_buy:
        raise ValueError("El precio de venta no puede ser menor al precio de compra")

    product = Product(
        name=product_data.name,
        description=product_data.description,
        price_buy=product_data.price_buy,
        price_sale=product_data.price_sale,
        stock=product_data.stock,
        status=True,  # activo por defecto
        id_category=product_data.id_category
    )

    db.add(product)
    db.commit()
    db.refresh(product)
    return product


# 📌 Actualizar producto
def update_product(db, product: Product, product_data: ProductUpdate):

    # Validar categoría
    category = db.query(Category).filter(Category.id == product_data.id_category).first()
    if not category:
        raise ValueError("La categoría no existe")

    # Validaciones
    if product_data.stock < 0:
        raise ValueError("El stock no puede ser negativo")

    if product_data.price_buy < 0 or product_data.price_sale < 0:
        raise ValueError("Los precios no pueden ser negativos")

    if product_data.price_sale < product_data.price_buy:
        raise ValueError("El precio de venta no puede ser menor al precio de compra")

    # Actualización
    product.name = product_data.name
    product.description = product_data.description
    product.price_buy = product_data.price_buy
    product.price_sale = product_data.price_sale
    product.stock = product_data.stock
    product.status = product_data.status
    product.id_category = product_data.id_category

    db.commit()
    db.refresh(product)
    return product


def delete_product(db, product: Product):
    product.status = False
    db.commit()
    return product


def calculate_margin(product: Product):
    return product.price_sale - product.price_buy
