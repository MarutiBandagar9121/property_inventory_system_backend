from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.location import LocationResponse, SublocationsResponse
from app.database import get_db
from app.services import location_service

router = APIRouter(tags=["Locations"])

@router.get("/locations", response_model=list[LocationResponse])
async def get_locations(db: Session = Depends(get_db)):
    try:
        locations = location_service.get_locations(db)
        return locations
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/sublocations", response_model=list[SublocationsResponse])
async def get_sublocations(db: Session = Depends(get_db)):
    try:
        sublocations = location_service.get_sublocations(db)
        return sublocations
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )