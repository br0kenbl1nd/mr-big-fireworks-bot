import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
    PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL", "")
    SUPPLY_MANAGER_NAME = os.getenv("SUPPLY_MANAGER_NAME", "Supply Manager")
    SUPPLY_MANAGER_PHONE = os.getenv("SUPPLY_MANAGER_PHONE", "")
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), "contacts.db")
    LOG_PATH = os.path.join(os.path.dirname(__file__), "logs", "app.log")

