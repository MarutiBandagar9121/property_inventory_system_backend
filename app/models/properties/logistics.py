from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Logistics(Base):
    __tablename__ = "logistics_details"

    id = Column(Integer, primary_key=True, index=True)

    node_id = Column(
        UUID,
        ForeignKey("property_nodes.id"),
        unique=True,
        nullable=False
    )

    logistics_name = Column(String(100), nullable=False)

    total_area = Column(Float, nullable=False)
    total_area_unit = Column(String(20), nullable=False)

    truck_bays = Column(Integer, nullable=True)
    loading_docks = Column(Integer, nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    property_node = relationship(
        "PropertyNode",
        back_populates="logistics"
    )