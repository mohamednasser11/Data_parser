from parsers.abstract_Handler import AbstractHandler
import xmltodict
import json
import random as rand

class XmlParsing(AbstractHandler):
    def parsing(self, file:str) -> str:
        if file.endswith('.xml'):
            with open(file, 'r', encoding='utf-8') as xmlFile:
                myXml = xmlFile.read()
            data = xmltodict.parse(myXml)
            return self.export_to_json(data,'xml/')
        else:
            return super().parsing(file)


#DV1581DVMC^24