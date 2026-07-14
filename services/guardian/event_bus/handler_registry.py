HANDLERS = {}

def register(event_name, handler):
    HANDLERS.setdefault(event_name, []).append(handler)
