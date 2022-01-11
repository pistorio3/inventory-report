from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import json
import csv


class Inventory:
    def generate_report(data, method):
        if method == "simples":
            return SimpleReport.generate(data)
        if method == "completo":
            return CompleteReport.generate(data)

    @classmethod
    def import_data(self, path, method):
        with open(path) as file:

            if path.endswith("csv"):
                data = csv.DictReader(file, delimiter=",")
                return self.generate_report([row for row in data], method)

            if path.endswith("json"):
                data = json.load(file)
                return self.generate_report(data, method)
