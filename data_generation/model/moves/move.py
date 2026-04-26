from abc import ABC, abstractmethod
from typing import List


class move(ABC):

    @abstractmethod
    def full_texts(self) -> List[str]:
        pass

    @abstractmethod
    def vectorize(self) -> List[float]:
        pass

    @abstractmethod
    def id(self) -> str:
        pass