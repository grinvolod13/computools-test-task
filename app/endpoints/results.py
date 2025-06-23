from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.usecases.results import ResultsUsecase
from app.dependency import get_session

router = APIRouter()


@router.get("/average")
def average(db: Session = Depends(get_session)):
    return ResultsUsecase(db).get()


@router.get("/average/{start_time}/{end_time}")
def average_filter(start_time: str, end_time: str, db: Session = Depends(get_session)):
    start: datetime = datetime.fromisoformat(start_time)
    end: datetime = datetime.fromisoformat(end_time)
    return ResultsUsecase(db).get(start, end)
