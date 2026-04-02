from sqlalchemy.orm import Session
from app.models.properties import NodeType


def seed_node_types(db: Session):
    types = [
        {"id": 1, "name": "BUILDING"},
        {"id": 2, "name": "WING"},
        {"id": 3, "name": "FLOOR"},
        {"id": 4, "name": "UNIT"},
        {"id": 5, "name": "LAND"},
        {"id": 6, "name": "INDUSTRIAL"},
        {"id": 7, "name": "LOGISTICS"},
        {"id": 8, "name": "RETAIL_UNIT"},
        {"id": 9, "name": "SHARED_OFFICE"},
    ]
    existing_ids = {row.id for row in db.query(NodeType.id).all()}
    for t in types:
        if t["id"] not in existing_ids:
            db.add(NodeType(**t))
    db.commit()
    print(f"  Node types seeded.")
