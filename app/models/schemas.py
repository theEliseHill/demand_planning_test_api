from pydantic import BaseModel, Field
from typing import List

class ForecastRequest(BaseModel):
    values: List[float]
    window: int = Field(8, ge=8, le=8)