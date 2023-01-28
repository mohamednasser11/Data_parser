from parsers.abstract_Handler import AbstractHandler
import xmltodict
from datetime import datetime

class XmlParsing(AbstractHandler):
    def parsing(self, file:str) -> str:
        name = file.split('.')[0]
        if file.endswith('.xml'):
            with open(file, 'r', encoding='utf-8') as xmlFile:
                myXml = xmlFile.read()
            data = xmltodict.parse(myXml)
            return self.export_to_json(data=data,destination='xml/', filename=name)
        else:
            return super().parsing(file)


#DV1581DVMC^24