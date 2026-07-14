from .provider.openai_provider import OpenAIProvider
from .provider.gemini_provider import GeminiProvider

PROVIDERS = {
    "openai": OpenAIProvider(),
    "gemini": GeminiProvider(),
}

def get_provider(name: str):
    return PROVIDERS.get(name.lower())
