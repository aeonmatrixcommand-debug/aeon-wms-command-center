from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs):
        pass

    @abstractmethod
    def health_check(self):
        pass
