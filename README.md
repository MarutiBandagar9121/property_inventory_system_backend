# create python venev
- python -m venv venv
- pip install -r requirements.txt
- uvicorn main:app --reload

- python -m pip freeze > requirements.txt

# Auto-generate a migration based on model changes
alembic revision --autogenerate -m ""

# Create an empty migration (for manual edits)
alembic revision -m ""

# Apply all pending migrations to the latest version
alembic upgrade head

# Apply a specific number of migrations
alembic upgrade +2  # Upgrade by 2 versions

# Upgrade to a specific revision
alembic upgrade <revision_id>