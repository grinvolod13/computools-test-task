from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import String
from datetime import datetime

from .base import Base

class Result(Base):
    """Benchmark result
    """
    __tablename__ = "result"
    request_id: Mapped[int] = mapped_column(primary_key=True)
    prompt_text: Mapped[str] = mapped_column(String(8000*8)) # for 8k tokens of length 8 (might be increased, this value is just for testing)
    generated_text: Mapped[str] = mapped_column(String(8000*8))
    token_count: Mapped[int]
    time_to_first_token: Mapped[int]
    time_per_output_token: Mapped[int]
    total_generation_time: Mapped[int]
    timestamp: Mapped[datetime]