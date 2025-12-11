from models.category import Category 

def get_all_categories(db):
    return db.query(Category).all()

def get_category_by_id(db, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db,data):
    new = Category(
        name = data.name,
        description = data.description,
        status = data.status
        )
    
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

def update_category(db, id,data):
    category = db.query(Category).filter(Category.id == id).first()

    if not category:
        return None
    
    if data.name:
        category.name = data.name
    db.merge(category)
    db.commit()
    db.refresh(category)
    return category

def delete_category(db, id):
   category = db.query(Category).filter(Category.id == id).first()
   if not category:
       return None
   
   category.status = False
   db.commit()
   db.refresh(category)
   return category

