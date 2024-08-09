from pydantic import BaseModel

class Event(BaseModel):
    type: str
    destination: str = None
    origin: str = None
    amount: int
