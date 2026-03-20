from app.database import Base
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

class Building(Base):
    __tablename__ = "buildings"

    id = Column(UUID, primary_key=True, index=True)
    node_id = Column(UUID, ForeignKey("property_nodes.id"), unique=True, nullable=False)
    building_name = Column(String(100), nullable=False)
    grade = Column(String(100), nullable=False)
    year_built = Column(Integer, nullable=False)
    total_area = Column(Float, nullable=False)
    total_area_unit = Column(String(20), nullable=False)
    power_backup = Column(Boolean, nullable=False)
    green_rating = Column(String(100), nullable=False)
    parking_ratio = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    property_node = relationship("PropertyNode", back_populates="building")