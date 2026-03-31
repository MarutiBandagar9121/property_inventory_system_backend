from sqlalchemy.orm import Session
from app.models.properties.location import Location
from app.models.properties.sublocation import Sublocation

def get_locations(db: Session):
    return db.query(Location).all()

def get_sublocations(db: Session):
    return db.query(Sublocation).all()