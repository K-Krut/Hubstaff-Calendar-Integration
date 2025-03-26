from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    GOOGLE_CREDENTIALS: str
    TOKEN_FILE: str
    CALENDAR_ID: str
    TIMEZONE: str

    HUBSTAFF_PERSONAL_ACCESS_TOKEN: str
    HUBSTAFF_API_URL: str
    HUBSTAFF_TOKENS: Path
    HUBSTAFF_USER_ID: int
    HUBSTAFF_ORG_ID: int

    @property
    def HUBSTAFF_TOKENS_PATH(self) -> Path:
        return (BASE_DIR / self.HUBSTAFF_TOKENS).resolve()

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
