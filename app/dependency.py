import contextlib
import os
from typing import Generator
import dotenv
dotenv.load_dotenv("./debug.env", override=False)



#--------------- Environment variables setup ---------------------#

if os.getenv("SUPERBENCHMARK_DEBUG", False) in ("True", True):
    DEBUG: bool = True
else:
    DEBUG: bool = False

DEBUG_CONNECTION_STRING: str = os.getenv("DEBUG_CONNECTION_STRING", "")
CONNECTION_STRING: str = os.getenv("CONNECTION_STRING", "")
DEBUG_DATA = "./test_database.json"

#--------------- Database connections, dependencies --------------#

from sqlalchemy import engine_from_config
from app.models import Base

if DEBUG:
    engine = engine_from_config({"sqlalchemy.url": DEBUG_CONNECTION_STRING})
else:
    engine = engine_from_config({"sqlalchemy.url": CONNECTION_STRING})
    
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker, Session

smaker = sessionmaker(engine)

def get_session()->Generator[Session, None, None]:
    session: Session = smaker()
    try:
        session.begin_nested()
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

get_session_contextmanager = contextlib.contextmanager(get_session)