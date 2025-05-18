from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_WHATSAPP_FROM: str
    STATUS_CALLBACK_URL: str
    WHATSAPP_WEBHOOK_URL: str

    class Config:
        env_file = ".env"

settings = Settings()