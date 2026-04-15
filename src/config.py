import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()


class Settings:
    def __init__(self):
        # ==================== Application Settings ====================
        self.APP_ENV = os.getenv("APP_ENV", "development")
        self.DEBUG = os.getenv("DEBUG", "true").lower() in ("true", "1", "yes")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

        # ==================== Server Settings ====================
        self.HOST = os.getenv("HOST", "0.0.0.0")
        self.PORT = int(os.getenv("PORT", 8000))

        # ==================== Database Settings ====================
        self.DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
        self.DB_PORT = int(os.getenv("DB_PORT", 5432))
        self.DB_NAME = os.getenv("DB_NAME", "inventory")
        self.DB_USER = os.getenv("DB_USER", "postgres")
        self.DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD", ""))

        # ==================== App Info ====================
        self.APP_NAME = "inventory-sales-system"
        self.APP_VERSION = "0.1.0"
        self.DESCRIPTION = (
            "Inventory and sales management system for small businesses with "
            "stock tracking, low-stock alerts, and sales analytics."
        )

    # ==================== DATABASE URL ====================
    @property
    def DATABASE_URL(self):
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    # ==================== VALIDATION ====================
    def validate(self):
        required_vars = {
            "DB_HOST": self.DB_HOST,
            "DB_USER": self.DB_USER,
            "DB_NAME": self.DB_NAME,
            "DB_PASSWORD": self.DB_PASSWORD,
        }

        missing = [key for key, value in required_vars.items() if not value]

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}"
            )

        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

        if self.LOG_LEVEL not in valid_log_levels:
            raise ValueError(f"Invalid LOG_LEVEL: {self.LOG_LEVEL}")

        if self.APP_ENV not in ["development", "production", "testing"]:
            raise ValueError(
                f"Invalid APP_ENV: {self.APP_ENV}. Must be development, production, or testing"
            )

        if self.APP_ENV == "production" and not self.DB_PASSWORD:
            raise ValueError("DB_PASSWORD required in production")

        if self.PORT < 1024 or self.PORT > 65535:
            raise ValueError(
                f"Invalid PORT: {self.PORT}. Must be between 1024 and 65535."
            )


# ==================== GLOBAL INSTANCE ====================
settings = Settings()
settings.validate()