from abc import abstractmethod
from parsers.reading_files_interface import ReadingFilesInterface
from typing import Optional
class AbstractHandler(ReadingFilesInterface):

    _next_parser:ReadingFilesInterface = None

    def set_next_parser(self, parser: ReadingFilesInterface) -> ReadingFilesInterface:
        self._next_parser = parser

        return parser
    
    @abstractmethod
    def parsing(self, file) -> Optional[str]:
        
        if self._next_parser:
            return self._next_parser.parsing(file)
        else:
            return None