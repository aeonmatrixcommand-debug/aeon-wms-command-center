from .base_provider import BaseProvider

class GeminiProvider(BaseProvider):
    def generate(self, prompt: str, **kwargs):
        raise NotImplementedError("Gemini integration pending")

    def health_check(self):
        return {"provider": "gemini", "status": "ready"}
