from services.guardian.ai_gateway.policy_engine import PolicyEngine


def test_gateway_flow():

    engine = PolicyEngine()

    decision = engine.evaluate({
        "classification": "normal"
    })

    assert decision.allowed is True
