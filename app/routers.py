from fastapi import APIRouter
from app.api import properties, nodes, cities, locations

api_router = APIRouter()

api_router.include_router(properties.router, prefix="/api/v1/properties")
api_router.include_router(nodes.router, prefix="/api/v1")
api_router.include_router(cities.router, prefix="/api/v1")
api_router.include_router(locations.router, prefix="/api/v1")
