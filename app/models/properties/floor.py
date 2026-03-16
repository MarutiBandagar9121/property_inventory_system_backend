from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class Floor(Base):
    __tablename__ = "floors"

    id = Column(UUID, primary_key=True, index=True)
    node_id = Column(UUID, ForeignKey("property_nodes.id"), nullable=False)
    floor_name = Column(String(100), nullable=False)
    floor_area = Column(Float, nullable=False)
    floor_area_unit = Column(String(10), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    property_node = relationship("PropertyNode", back_populates="floor")