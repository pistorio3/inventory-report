from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(file_name):
        if not file_name.endswith("csv"):
            raise ValueError("Arquivo inválido")
        with open(file_name) as file:
            data = csv.DictReader(file, delimiter=",")
            return [row for row in data]
