### Input validation with pydantic:

from pydantic import BaseModel, Field

class MathResult(BaseModel):
    number:float
    result:float
    operation:str