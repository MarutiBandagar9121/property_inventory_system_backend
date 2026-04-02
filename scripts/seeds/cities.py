from sqlalchemy.orm import Session
from app.models.properties import City


def seed_cities(db: Session):
    cities = [
        {"id": 1, "name": "Pune",      "state": "Maharashtra", "short_name": "Pune"},
        {"id": 2, "name": "Mumbai",    "state": "Maharashtra", "short_name": "Mumbai"},
        {"id": 3, "name": "Nagpur",    "state": "Maharashtra", "short_name": "Nagpur"},
        {"id": 4, "name": "Banglore",  "state": "Karnataka",   "short_name": "Banglore"},
        {"id": 5, "name": "Hyderabad", "state": "Telangana",   "short_name": "Hyderabad"},
        {"id": 6, "name": "Chennai",   "state": "Tamil Nadu",  "short_name": "Chennai"},
    ]
    existing_ids = {row.id for row in db.query(City.id).all()}
    for c in cities:
        if c["id"] not in existing_ids:
            db.add(City(**c))
    db.commit()
    print(f"  Cities seeded.")
