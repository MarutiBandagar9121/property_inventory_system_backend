from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, Float, Integer, String, ForeignKey

class Unit(Base):
    __tablename__ = "units"

    id = Column(UUID, primary_key=True, index=True)
    node_id = Column(UUID, ForeignKey("property_nodes.id"), nullable=False)
    # unit details
    unit_name = Column(String(100), nullable=False)
    unit_area = Column(Float, nullable=False)
    unit_area_unit = Column(String(10), nullable=False)
    # chargeable area
    chargeable_area = Column(Float, nullable=False)
    chargeable_area_unit = Column(String(10), nullable=False)
    # carpet area
    carpet_area = Column(Float, nullable=False)
    carpet_area_unit = Column(String(30), nullable=False)
    # rental
    rental = Column(Float, nullable=False)
    rental_unit = Column(String(30), nullable=False)
    # notice period
    notice_period = Column(Integer, nullable=False)
    notice_period_unit = Column(String(30), nullable=False)
    # cam charges
    cam_charges = Column(Float, nullable=False)
    cam_charges_unit = Column(String(30), nullable=False)
    # timestampa
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    property_node = relationship("PropertyNode", back_populates="unit")