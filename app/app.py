from fastapi import FastAPI
from sqlalchemy.exc import IntegrityError

from app import dependency
from app.endpoints import result_router
from app.utils import load_debug_db


# ------------------- Debug mode setup -----------------------#

if not dependency.DEBUG:
    raise NotImplementedError("Feature is not ready for live yet")
else:
    try:
        with dependency.get_session_contextmanager() as s:
            load_debug_db(s, dependency.DEBUG_DATA)  # Loads data fro, json
    except IntegrityError:
        pass


# ------------------- FastApi instance setup -----------------#

app = FastAPI()
app.include_router(
    result_router,
    prefix="/results",
)
