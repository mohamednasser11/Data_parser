from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class ReadingFilesInterface(ABC):
    @abstractmethod
    def set_next_parser(self, parser:ReadingFilesInterface) -> ReadingFilesInterface:
        pass

    @abstractmethod
    def parsing(self, file) -> Optional[str]:
        pass