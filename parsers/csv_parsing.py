from parsers.abstract_Handler import AbstractHandler

class CsvParsing(AbstractHandler):
    def parsing(self, file:str) -> str:
        if file.endswith('.csv'):
            print('CSV')
        else:
            return super().parsing(file)