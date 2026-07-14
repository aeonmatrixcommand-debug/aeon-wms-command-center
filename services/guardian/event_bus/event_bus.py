class EventBus:
    def __init__(self):
        self._handlers = {}

    def subscribe(self, event_name, handler):
        self._handlers.setdefault(event_name, []).append(handler)

    def publish(self, event):
        for handler in self._handlers.get(event.name, []):
            handler(event)
