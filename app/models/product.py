from sqlalchemy import ForeinKey
from sqlalchemy import string
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column,declarative_base

class Product(Base)::
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    price_sale: Mapped[float] = mapped_column(nullable=False)
    price_buy: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(nullable=False)
    stock_min: Mapped[int] = mapped_column(nullable=False, default=0)
    id_category: Mapped[int] = mapped_column(ForeinKey("categories.id"), nullable=False)
    status: Mapped[bool] = mapped_column(nullable=False, default=True)
    category: Mapped["Category"] = relationship(back_populates="products")
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    