import json
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.results import Result


def load_debug_db(session: Session, filepath: str):
    """Loads data to db from json"""
    with open(filepath) as f:
        data: dict = json.load(f)

    for item in data["benchmarking_results"]:
        item["timestamp"] = datetime.fromisoformat(item["timestamp"])
        session.add(Result(**item))
    session.commit()
