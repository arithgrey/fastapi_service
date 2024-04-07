from abc import ABC, abstractmethod

class DatabaseConfig(ABC):
    @abstractmethod
    def get_database_url(self) -> str:
        pass
