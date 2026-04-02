from uuid import uuid4
from app.database import Base
from sqlalchemy import Column, DateTime, Index, Integer, Numeric, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class Property(Base):
    __tablename__ = "properties"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    property_name = Column(String(100), nullable=False)
    property_grade = Column(String(100), nullable=True)
    
    # Foreign Keys - ALL indexed for JOIN performance
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False, index=True)
    sublocation_id = Column(Integer, ForeignKey("sublocations.id"), nullable=True, index=True)
    property_type_id = Column(Integer, ForeignKey("property_types.id"), nullable=False, index=True)
    
    # Other columns (
    latitude = Column(Numeric(9,6), nullable=True)
    longitude = Column(Numeric(9,6), nullable=True)
    google_map_url = Column(String(500), nullable=True)
    address_line1 = Column(String(100), nullable=False)
    address_line2 = Column(String(100), nullable=True)
    postal_code = Column(String(20), nullable=True)
    total_property_area = Column(Numeric(10,2), nullable=True)
    tenant_profile = Column(String(200), nullable=True)

    # Relationships
    city = relationship("City", back_populates="properties")
    location = relationship("Location", back_populates="properties")
    sublocation = relationship("Sublocation", back_populates="properties")
    property_type = relationship("PropertyType", back_populates="properties")
    
    # Composite indexes for common query combinations
    __table_args__ = (
        # filter by city AND location together
        Index('idx_property_city_location', 'city_id', 'location_id'),
        
        # filter by property_type AND city together
        Index('idx_property_type_city', 'property_type_id', 'city_id'),
    )

class PropertyType(Base):
    __tablename__ = "property_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    properties = relationship("Property", back_populates="property_type")

class NodeType(Base):
    __tablename__ = "node_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    property_nodes = relationship("PropertyNode", back_populates="node_type")

class PropertyNode(Base):
    __tablename__ = "property_nodes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    node_name = Column(String(100), nullable=False)
    property_id = Column(UUID(as_uuid=True), ForeignKey("properties.id"), nullable=False, index=True)
    node_type_id = Column(Integer, ForeignKey("node_types.id"), nullable=False, index=True)
    parent_node_id = Column(UUID(as_uuid=True), ForeignKey("property_nodes.id"), nullable=True, index=True)
    sequence_order = Column(Integer, nullable=False)
    status = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    node_type = relationship("NodeType", back_populates="property_nodes")
    parent_node = relationship("PropertyNode", remote_side=[id], back_populates="child_nodes")
    child_nodes = relationship("PropertyNode", back_populates="parent_node",cascade="all, delete-orphan")

    building = relationship(
        "Building", 
        back_populates="property_node",
        uselist=False)
    
    wing = relationship(
        "Wing",
        back_populates="property_node",
        uselist=False
    )

    floor = relationship(
        "Floor",
        back_populates="property_node",
        uselist=False
    )

    unit = relationship(
        "Unit",
        back_populates="property_node",
        uselist=False
    )

    land = relationship(
        "Land",
        back_populates="property_node",
        uselist=False
    )

    industrial = relationship(
        "Industrial",
        back_populates="property_node",
        uselist=False
    )

    logistics = relationship(
        "Logistics",
        back_populates="property_node",
        uselist=False
    )

    retail_unit = relationship(
        "RetailUnit",
        back_populates="property_node",
        uselist=False
    )

    __table_args__ = (
        # Composite index for common queries
        Index('idx_property_node_hierarchy', 'property_id', 'parent_node_id', 'sequence_order'),
        # Index for ordering within same parent
        Index('idx_node_ordering', 'parent_node_id', 'sequence_order'),
    )