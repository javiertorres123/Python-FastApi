from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import base

if TYPE_CHECKING:
    from app.models.product import Product

class Category(base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    status: Mapped[bool] = mapped_column(nullable=False, default=True)
    products: Mapped[list["Product"]] = relationship(back_populates="category")
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)