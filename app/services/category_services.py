from models.category import Category

def get_all_categories(db):
    return db.query(Category).all()

def get_category_by_id(db, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db, category: Category):
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(db, category: Category):
    db.merge(category)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db, category: Category):
    db.delete(category)
    db.commit()
    return category

