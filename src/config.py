import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # ==================== Application Settings ====================
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() in ("true", "1", "yes")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()

    # ==================== Server Settings ====================
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))

    # ==================== Database Settings ====================
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME", "Inventory")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")

    # Async PostgreSQL Database URL
    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    # ==================== Application Metadata ====================
    APP_NAME: str = "inventory-sales-system"
    APP_VERSION: str = "0.1.0"
    DESCRIPTION: str = (
        "Inventory and sales management system for small businesses with "
        "stock tracking, low-stock alerts, and sales analytics."
    )

    @classmethod
    def validate(cls):
        """Validate required configuration values"""
        required_vars = ["DB_HOST", "DB_USER", "DB_NAME", "DB_PASSWORD"]
        missing = [var for var in required_vars if not getattr(cls, var, None)]

        if missing:
            raise ValueError(
                (
                    f"Missing required environment variables: "
                    f"{', '.join(missing)}\n"
                    "Please check your .env file."
                )
            )
        valid_log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

        if cls.LOG_LEVEL not in valid_log_levels:
            raise ValueError(f"Invalid LOG_LEVEL: {cls.LOG_LEVEL}")
        if cls.APP_ENV not in ["development", "production", "testing"]:
            raise ValueError(
                f"Invalid APP_ENV: {cls.APP_ENV}. Must be one of: "
                "development, production, testing"
            )

        if cls.PORT < 1024 or cls.PORT > 65535:
            raise ValueError(
                f"Invalid PORT: {cls.PORT}. Must be between 1024 and 65535."
            )


# Create a global settings instance
settings = Settings()
