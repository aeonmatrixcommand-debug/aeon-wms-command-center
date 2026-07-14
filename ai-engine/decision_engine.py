class AIDecisionEngine:

    def analyze(self, event):

        if event["type"] == "NO_SCAN":
            return {
                "action": "BLOCK_MOVEMENT",
                "confidence": 1.0,
                "reason": "No Scan No Move violation"
            }

        if event["type"] == "SHORT_PICK":
            return {
                "action": "REPLENISH_STOCK",
                "confidence": 0.92,
                "reason": "Stock shortage detected"
            }

        return {
            "action": "MONITOR",
            "confidence": 0.5
        }


if __name__ == "__main__":

    engine = AIDecisionEngine()

    test_event = {
        "type": "NO_SCAN"
    }

    print(engine.analyze(test_event))
