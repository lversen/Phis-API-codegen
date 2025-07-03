
from pydantic import BaseModel, Field
from typing import Optional

class Ref(BaseModel):
    description: Optional[str] = Field(description="CSV import settings")
