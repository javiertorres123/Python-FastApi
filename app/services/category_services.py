from models.category import Category
from models.product import Product


# 📌 Listar solo categorías activas
def get_all_categories(db):
    return db.query(Category).filter(Category.status == True).all()


# 📌 Obtener categoría con sus productos
def get_category_by_id(db, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise ValueError("La categoría no existe")

    # Los productos ya vienen por la relación
    return category


# 📌 Crear categoría
def create_category(db, data):

    # Evitar nombres duplicados
    existing = db.query(Category).filter(Category.name == data.name).first()
    if existing:
        raise ValueError("Ya existe una categoría con ese nombre")

    new_category = Category(
        name=data.name,
        description=data.description,
        status=True  # activa por defecto
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


# 📌 Actualizar categoría
def update_category(db, category_id: int, data):

    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise ValueError("La categoría no existe")

    # Validar nombre duplicado (otro ID)
    if data.name and data.name != category.name:
        existing = db.query(Category).filter(Category.name == data.name).first()
        if existing and existing.id != category.id:
            raise ValueError("Ya existe una categoría con ese nombre")

    # Actualizar campos
    category.name = data.name
    category.description = data.description

    db.commit()
    db.refresh(category)
    return category


# 📌 Desactivar categoría (soft delete)
def delete_category(db, category_id: int):

    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise ValueError("La categoría no existe")

    # No permitir desactivar si tiene productos activos
    active_products = (
        db.query(Product)
        .filter(Product.id_category == category.id, Product.status == True)
        .all()
    )

    if active_products:
        raise ValueError(
            "No se puede desactivar la categoría porque tiene productos activos asociados"
        )

    category.status = False
    db.commit()
    db.refresh(category)
    return category
