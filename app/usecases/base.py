from typing import Self
from sqlalchemy.orm import Session


class BaseUsecase:
    def __init__(self, db: Session) -> Self:  # type: ignore
        self._db = db
