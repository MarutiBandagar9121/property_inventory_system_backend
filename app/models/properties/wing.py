from app.database import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


class Wing(Base):
    __tablename__ = "wings"

    id = Column(Integer, primary_key=True, index=True)
    node_id = Column(UUID, ForeignKey("property_nodes.id"), nullable=False)
    wing_name = Column(String(100), nullable=False)
    independent_entrance = Column(Boolean, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    property_node = relationship("PropertyNode", back_populates="wing")