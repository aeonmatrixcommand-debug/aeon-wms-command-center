from services.guardian.ai_gateway.registry.provider_registry import ProviderRegistry


def test_provider_health():

    registry = ProviderRegistry()

    registry.register(
        "openai",
        "provider",
        {
            "status": "healthy",
            "latency": 220
        }
    )

    assert registry.health()["openai"] == "healthy"
