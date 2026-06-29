from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    App configuration using Pydantic Settings.
    It automatically reads environment variables from the .env file.
    """
    gemini_api_key: str

    # Configuration to tell pydantic to look for a .env file
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

# Create a global instance of settings to be used throughout the app
settings = Settings()