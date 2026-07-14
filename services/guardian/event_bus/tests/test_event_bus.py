from services.guardian.event_bus.event_bus import EventBus
from services.guardian.event_bus.event import Event

def test_publish():
    bus = EventBus()
    called = []

    def handler(event):
        called.append(event.name)

    bus.subscribe("telemetry.received", handler)
    bus.publish(Event("telemetry.received", "test", {}))

    assert called == ["telemetry.received"]
