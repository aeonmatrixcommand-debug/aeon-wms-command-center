class EventGateway:
    def publish(self, topic, payload):
        return {
            "topic": topic,
            "payload": payload,
            "status": "published"
        }
