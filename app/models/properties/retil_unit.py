from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class RetailUnit(Base):
    __tablename__ = "retail_units"

    id = Column(Integer, primary_key=True, index=True)

    node_id = Column(
        UUID,
        ForeignKey("property_nodes.id"),
        unique=True,
        nullable=False
    )

    retail_unit_name = Column(String(100), nullable=False)

    unit_area = Column(Float, nullable=False)
    unit_area_unit = Column(String(20), nullable=False)

    frontage = Column(Float, nullable=True)

    rental = Column(Float, nullable=True)
    rental_unit = Column(String(20), nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    property_node = relationship(
        "PropertyNode",
        back_populates="retail_unit"
    )