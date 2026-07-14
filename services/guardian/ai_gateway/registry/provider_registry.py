class ProviderRegistry:

    def __init__(self):
        self.providers = {}

    def register(self, name, provider, metadata=None):
        self.providers[name] = {
            "provider": provider,
            "metadata": metadata or {}
        }

    def get(self, name):
        return self.providers.get(name)

    def health(self):
        return {
            name: data["metadata"].get("status", "unknown")
            for name, data in self.providers.items()
        }
