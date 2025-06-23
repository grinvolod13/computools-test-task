from typing import Self
from sqlalchemy import column, select, Select
from sqlalchemy.orm import Session, Bundle
from sqlalchemy.sql import func, select
from datetime import datetime

from .base import BaseUsecase
from app.models import Result


class ResultsUsecase(BaseUsecase):
    def __init__(self, db: Session):
        super().__init__(db)

    def get(
        self,
        start: datetime | None = None,
        end: datetime | None = None,
    ):

        stm: Select = select(
            Bundle(
                "results",
                func.avg(column("token_count")).label("avg_token_count"),
                func.avg(Result.time_to_first_token).label("avg_time_to_first_token"),
                func.avg(Result.time_per_output_token).label(
                    "avg_time_per_output_token"
                ),
                func.avg(Result.total_generation_time).label("avg_generation_time"),
            )
        )

        if start:
            stm = stm.where(Result.timestamp >= start)
        if end:
            stm = stm.where(Result.timestamp <= end)
        data = list(self._db.execute(stm).scalars().one())
        response = dict()
        response["avg_token_count"] = data[0]
        response["avg_time_to_first_token"] = data[1]
        response["avg_time_per_output_token"] = data[2]
        response["avg_generation_time"] = data[3]

        return response
