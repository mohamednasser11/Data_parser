from abc import abstractmethod
from parsers.reading_files_interface import ReadingFilesInterface
from typing import Optional
from datetime import datetime
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
    
    
    def export_to_json(self,filename:str, data, destination:str):
        filename = self.generate_filename(file=filename)
        filepath = Path(r"./output/"+destination+filename)
        filepath.parent.mkdir(parents=True,exist_ok=True)
        with open(filepath, 'w') as file:
            json.dump(data,file, indent=4)
        print('Exporting Done')

    def generate_filename(self,file:str):
        filename = ''
        filename = file.split('/')[len(filename)-1].split('.')[0]
        ts = str(datetime.timestamp(datetime.now()))
        filename = ts + filename +'.json'
        return filename