from src.config import settings

def test_gemini_api_key_is_configured():

    assert isinstance(settings.gemini_api_key, str)
    
    assert len(settings.gemini_api_key) > 0, "The API key should not be empty."