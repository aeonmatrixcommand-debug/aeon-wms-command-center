from services.guardian.ai_gateway.policy_engine import PolicyEngine


def test_policy_engine_exists():
    engine = PolicyEngine()
    assert engine is not None
