from parsers.xml_parsing import XmlParsing
from parsers.csv_parsing import CsvParsing
from parsers.json_parser import JsonParsing


class Handler:

    def __init__(self, request):
        xml_parser = XmlParsing()
        csv_parser = CsvParsing()
        json_parser = JsonParsing()

        xml_parser.set_next_parser(csv_parser)\
            .set_next_parser(json_parser)
        xml_parser.parsing(file=request)
