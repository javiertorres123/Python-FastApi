from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column, declarative_base

# Import Category from its module (adjust the import path as needed)
from .category import Category

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    price_sale: Mapped[float] = mapped_column(nullable=False)
    price_buy: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(nullable=False)
    id_category: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    status: Mapped[bool] = mapped_column(nullable=False, default=True)
    category: Mapped["Category"] = relationship(back_populates="products")
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    