
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base

class Sublocation(Base):
    __tablename__ = "sublocations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("name", "location_id", name="uq_sublocation_name_location"),
    )
    
    location = relationship("Location", back_populates="sublocations")
    properties = relationship("Property", back_populates="sublocation")