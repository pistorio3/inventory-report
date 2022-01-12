from inventory_report.importer.importer import Importer
import xmltodict
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(file_name):
        if not file_name.endswith("xml"):
            raise ValueError("Arquivo inválido")
        with open(file_name) as file:
            root = ET.parse(file).getroot()
            data = xmltodict.parse(
                ET.tostring(root, encoding="utf8", method="xml")
            )
            return data["dataset"]["record"]
