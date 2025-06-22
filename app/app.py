from fastapi import FastAPI, Depends

from app import dependency
from app.endpoints import result_router

if not dependency.DEBUG:
    raise NotImplementedError("Feature is not ready for live yet")
else:
    # TODO: load data from test json to db
    ...

app = FastAPI()
app.include_router(
    result_router,
    prefix="/results",
    dependencies=[Depends(dependency.get_session)]
    )

