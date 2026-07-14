from services.guardian.ai_gateway.registry.provider_registry import ProviderRegistry


def test_provider_registry_exists():
    registry = ProviderRegistry()
    assert registry is not None
