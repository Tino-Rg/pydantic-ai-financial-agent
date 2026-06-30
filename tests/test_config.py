"""
Tests for the configuration module.
Ensures that environment variables and application settings are correctly loaded.
"""
from src.config import settings


def test_gemini_api_key_is_configured():
    """
    Verifies that the Gemini API key is properly loaded from the environment 
    and is not an empty string.
    """
    assert isinstance(settings.gemini_api_key, str)
    assert len(settings.gemini_api_key) > 0, "The API key should not be empty."