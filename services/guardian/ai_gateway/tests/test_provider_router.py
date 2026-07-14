from services.guardian.ai_gateway.provider_router import get_provider

def test_router():
    assert get_provider("openai") is not None
    assert get_provider("gemini") is not None
