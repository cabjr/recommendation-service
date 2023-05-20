from pydantic import BaseModel
from typing import Any, Dict

class Item(BaseModel):
    features: Dict[str, Any]
    label: float = None
