from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_generate = super().generate(list=list)
        companies = []

        for product in list:
            companies.append(
                (
                    product["nome_da_empresa"],
                    cls.count_company_appears(
                        product["nome_da_empresa"],
                        list
                    )
                )
            )

        message = "Produtos estocados por empresa: \n"

        listed_companies = []

        for company in companies:
            try:
                listed_companies.index(company[0])
            except ValueError:
                listed_companies.append(company[0])
                message += f"- {company[0]}: {company[1]}\n"

        return simple_generate + "\n" + message
