from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    GOOGLE_CREDENTIALS: str
    TOKEN_FILE: str

    HUBSTAFF_PERSONAL_ACCESS_TOKEN: str
    HUBSTAFF_API_URL: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()