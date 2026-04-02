"""
Run this script after `alembic upgrade head` to populate lookup/reference data.
Safe to re-run — all seeders are idempotent.

Usage:
    python scripts/seed.py
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from scripts.seeds.cities import seed_cities
from scripts.seeds.locations import seed_locations
from scripts.seeds.sublocations import seed_sublocations
from scripts.seeds.property_types import seed_property_types
from scripts.seeds.node_types import seed_node_types


def main():
    db = SessionLocal()
    try:
        print("Seeding cities...")
        seed_cities(db)

        print("Seeding locations...")
        seed_locations(db)

        print("Seeding sublocations...")
        seed_sublocations(db)

        print("Seeding property types...")
        seed_property_types(db)

        print("Seeding node types...")
        seed_node_types(db)

        print("Done.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
