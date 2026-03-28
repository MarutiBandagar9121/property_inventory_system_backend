# Property Inventory Management System

> A production-grade, enterprise-ready backend API for commercial real estate operations — built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy 2.0**.

---

## What Is This?

A robust backend system built for real estate advisory and brokerage firms to manage their entire property portfolio, workforce, and sales pipeline — all in one place. Consumed by an internal **employee/admin app (React)** for staff operations. A customer-facing app is planned for a future phase.

---

## Core Modules

### Property Inventory Management
The centerpiece of the system. Properties are modeled as a **hierarchical node tree** — not a flat table — enabling complex, real-world asset structures:

```
Property
  └── Building
        └── Wing
              └── Floor
                    └── Unit / Retail Unit
  └── Land
  └── Industrial
  └── Logistics
```

This design supports all major commercial real estate verticals:
- Office Space (traditional + coworking/shared)
- Retail Space
- Industrial Space
- Logistics & Warehousing
- Land Deals
- Investment Assets

One property can hold multiple simultaneous offerings (lease, sale, investment) without ever duplicating the physical asset.

### Role-Based Employee Management
A multi-tier access control system with granular employee roles:

| Role | Description |
|------|-------------|
| `SUPER_ADMIN` | Full system access, app config, user provisioning |
| `OFFICE_HEAD` | Oversees regional operations and team leads |
| `TRANSACTION_MANAGER` | Manages deal flow and closings |
| `BUSINESS_DEVELOPMENT_MANAGER` | Handles lead pipeline and client relations |
| `DATA_MANAGER` | Manages property data quality and approvals |
| `DATA_SURVEYOR` | Field-level data entry and property surveying |

### Lead Management
Full CRM integration with **Zoho CRM** — webhook ingestion and bidirectional API sync — ensuring every lead is tracked, assigned, and actioned without manual overhead.

### Super Admin Interface
A dedicated configuration layer for provisioning and managing the entire application:
- System-wide settings and app config
- User creation and role assignment
- Lookup table management (cities, locations, node types, property types)

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI (Python 3.13) |
| Database | **PostgreSQL** |
| ORM | SQLAlchemy 2.0 (async-ready, modern `select()` API) |
| Schema Validation | Pydantic v2 |
| DB Migrations | Alembic |
| Server | Uvicorn |
| Config | pydantic-settings + `.env` |

### Why PostgreSQL?

Because this system demands it. A hierarchical property node tree, multi-role access control, CRM sync, and concurrent offerings on a single asset — this is not a job for something lightweight. PostgreSQL brings rock-solid ACID compliance, native support for complex relational queries, powerful indexing, and the kind of battle-tested reliability that enterprise real estate data deserves. Not a compromise in sight.

---

## Project Structure

```
app/
  config.py          # App settings via pydantic-settings
  database.py        # SQLAlchemy engine, SessionLocal, get_db()
  models/
    properties/      # Property node tree SQLAlchemy models
    users/           # User and role models
  routers/           # One router file per domain
  schemas/           # Pydantic request/response schemas
  services/          # Business logic layer (routes stay thin)
alembic/             # DB migration scripts
main.py              # FastAPI app entry point
```

---

## Getting Started

### 1. Clone & set up the environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/property_db
```

### 3. Run database migrations

```bash
alembic upgrade head
```

### 4. Start the development server

```bash
uvicorn main:app --reload
```

API docs available at `http://localhost:8000/docs`

---

## Database Migrations (Alembic)

```bash
# Auto-generate a migration from model changes
alembic revision --autogenerate -m "describe your change"

# Create an empty migration for manual edits
alembic revision -m "describe your change"

# Apply all pending migrations
alembic upgrade head

# Upgrade by a specific number of steps
alembic upgrade +2

# Upgrade to a specific revision
alembic upgrade <revision_id>

# Roll back the last migration
alembic downgrade -1
```

---

## Saving Dependencies

```bash
pip freeze > requirements.txt
```

---

## API Documentation

FastAPI auto-generates interactive API docs out of the box:
- **Swagger UI** — `http://localhost:8000/docs`
- **ReDoc** — `http://localhost:8000/redoc`
