from parsers.abstract_Handler import AbstractHandler

class XmlParsing(AbstractHandler):
    def parsing(self, file:str) -> str:
        if file.endswith('.xml'):
             print('Xml')
        else:
            return super().parsing(file)