from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    app_name: str = "Math API"          
    debug: bool = False                  
    version: str = "1.0.0"              
    allowed_origins: List[str] = ["*"]  

    model_config = {"env_file": ".env"}
settings = Settings()