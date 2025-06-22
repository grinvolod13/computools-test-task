from fastapi import FastAPI

import app.dependency
from app.endpoints import result_router

if not app.dependency.DEBUG:
    raise NotImplementedError("Feature is not ready for live yet")
else:
    # TODO: load data from test json to db
    ...

app = FastAPI()
app.include_router(result_router, prefix="/results")

