
from datetime import date
from pydantic import BaseModel

class NewUser(BaseModel):
    name: str
    email: str
    birth_date: date
    sennior_client: bool
    subscripted_date: date