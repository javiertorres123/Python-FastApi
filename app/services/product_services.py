from app.models.product import Product

def get_all_products(db):
    return db.query(Product).all()

def get_product_by_id(db, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db, product: Product):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update_product(db, product: Product):
    db.merge(product)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db, product: Product):
    db.delete(product)
    db.commit()
    return product

