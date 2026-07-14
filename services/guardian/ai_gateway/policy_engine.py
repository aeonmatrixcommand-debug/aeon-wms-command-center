class PolicyEngine:

    def __init__(self):
        self.name = "AI Gateway Policy Engine"

    def evaluate(self, request):
        return {
            "allowed": True,
            "reason": "policy_pass"
        }
