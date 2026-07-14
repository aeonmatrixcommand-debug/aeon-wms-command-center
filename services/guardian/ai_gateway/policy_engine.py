from dataclasses import dataclass


@dataclass
class PolicyDecision:
    allowed: bool
    risk_score: int
    reason: str
    policy_id: str


class PolicyEngine:

    def __init__(self):
        self.name = "AI Gateway Policy Engine v2"

    def evaluate(self, request):

        risk_score = 15

        if request.get("classification") == "sensitive":
            risk_score = 80

        allowed = risk_score < 90

        return PolicyDecision(
            allowed=allowed,
            risk_score=risk_score,
            reason="policy_pass" if allowed else "risk_block",
            policy_id="AI-GOV-001"
        )
