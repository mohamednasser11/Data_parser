from parsers.abstract_Handler import AbstractHandler

class JsonParsing(AbstractHandler):
    def parsing(self, file:str) -> str:
        if file.endswith('.json'):
            print('Json')
        else:
            return super().parsing(file)