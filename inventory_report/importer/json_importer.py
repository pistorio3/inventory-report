from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(file_name):
        if not file_name.endswith("json"):
            raise ValueError("Arquivo inválido")
        with open(file_name) as file:
            data = json.load(file)
            return data
