from app.database import Base
from sqlalchemy import UUID, Column, DateTime, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(100), nullable=False)
    project_grade = Column(String(100), nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    sublocation_id = Column(Integer, ForeignKey("sublocations.id"), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    google_map_url = Column(String(500), nullable=False)
    address_line1 = Column(String(100), nullable=False)
    address_line2 = Column(String(100),nullable=True)
    total_property_area = Column(Float, nullable=False)
    total_property_area_unit = Column(String(20), nullable=False)
    property_sanction_type = Column(String(100), nullable=False)
    tenant_profile = Column(String(500), nullable=True)
    property_type_id = Column(Integer,ForeignKey("property_types.id"), nullable=False)
    city = relationship("City", back_populates="properties")
    location = relationship("Location", back_populates="properties")
    sublocation = relationship("Sublocation", back_populates="properties")
    property_type = relationship("PropertyType", back_populates="properties")

class PropertyType(Base):
    __tablename__ = "property_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)

    properties = relationship("Property", back_populates="property_type")

class NodeType(Base):
    __tablename__ = "node_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)

    property_nodes = relationship("PropertyNode", back_populates="node_type")

class PropertyNode(Base):
    __tablename__ = "property_nodes"

    id = Column(UUID, primary_key=True, index=True)
    node_name = Column(String(100), nullable=False)
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=False)
    node_type_id = Column(Integer, ForeignKey("node_types.id"), nullable=False)
    parent_node_id = Column(UUID, ForeignKey("property_nodes.id"), nullable=True)
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