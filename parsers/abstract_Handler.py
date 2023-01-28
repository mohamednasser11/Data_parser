from abc import abstractmethod
from parsers.reading_files_interface import ReadingFilesInterface
from typing import Optional
import random as rand
from pathlib import Path
import json
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
    
    
    def export_to_json(self, data,destination:str):
        randname = self.random_filename()
        filename = randname
        filepath = Path(r"./output/"+destination+filename)
        filepath.parent.mkdir(parents=True,exist_ok=True)
        with open(filepath, 'w') as file:
            json.dump(data,file, indent=4)
        print('Exporting Done')

    def random_filename(self):
        filename = "file.json"
        enc = ''
        for i in range(0,15):
            num = rand.randint(0,10)
            enc += str(num)
        filename = enc + filename
        return filename