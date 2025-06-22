import os
import dotenv
dotenv.load_dotenv("./debug.env", override=False)


if _debug:=os.getenv("SUPERBENCHMARK_DEBUG", False) in ("True", True):
    DEBUG: bool = True
else:
    DEBUG: bool = False

TEST_DATA = "./test_database.json"