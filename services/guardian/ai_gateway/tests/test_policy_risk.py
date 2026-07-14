from services.guardian.ai_gateway.policy_engine import PolicyEngine


def test_sensitive_request_risk():

    engine = PolicyEngine()

    result = engine.evaluate({
        "classification": "sensitive"
    })

    assert result.risk_score == 80
