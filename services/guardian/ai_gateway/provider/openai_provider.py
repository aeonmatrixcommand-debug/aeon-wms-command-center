from .base_provider import BaseProvider

class OpenAIProvider(BaseProvider):
    def generate(self, prompt: str, **kwargs):
        raise NotImplementedError("OpenAI integration pending")

    def health_check(self):
        return {"provider": "openai", "status": "ready"}
