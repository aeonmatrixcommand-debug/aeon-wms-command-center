class MessageDispatcher:
    def dispatch(self, event):
        return {"status": "dispatched", "event": event}
