from sqlalchemy.orm import Session
from app.models.properties import PropertyType


def seed_property_types(db: Session):
    types = [
        {"id": 1, "name": "Office_Commercial_Space"},
        {"id": 2, "name": "Standalone_Retail"},
        {"id": 3, "name": "Mall"},
        {"id": 4, "name": "Land"},
        {"id": 5, "name": "Logistics"},
        {"id": 6, "name": "Industrial"},
    ]
    existing_ids = {row.id for row in db.query(PropertyType.id).all()}
    for t in types:
        if t["id"] not in existing_ids:
            db.add(PropertyType(**t))
    db.commit()
    print(f"  Property types seeded.")
