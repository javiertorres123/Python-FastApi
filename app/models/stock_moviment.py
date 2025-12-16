from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column, declarative_base
from app.core.database import base

if TYPE_CHECKING:
    from app.models.product import Product

class StockMoviment(base):
    __tablename__ = "stock_moviments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    id_product: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    movement_type: Mapped[str] = mapped_column(String(50), nullable=False)  
    reason: Mapped[str] = mapped_column(String(255), nullable=True)
    stock_after: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[bool] = mapped_column(nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)

    product: Mapped["Product"] = relationship()