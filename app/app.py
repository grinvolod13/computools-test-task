from fastapi import FastAPI

from app.endpoints import result_router


app = FastAPI()
app.include_router(result_router, prefix="result")
