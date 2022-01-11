from datetime import date


class SimpleReport:
    def count_company_appears(name, list):
        company_appears = 0
        for info in list:
            if info["nome_da_empresa"] == name:
                company_appears += 1
        return company_appears

    @classmethod
    def generate(cls, list):
        today = date.today()

        earliest_manufacturing_date = date.max
        closest_expiration_date = date.max

        bigger_stock_company = ""
        products_in_stock = 0

        for product in list:

            product_fab_date = date.fromisoformat(
                product["data_de_fabricacao"]
            )

            product_exp_date = date.fromisoformat(
                product["data_de_validade"]
            )

            if product_fab_date < earliest_manufacturing_date:
                earliest_manufacturing_date = product_fab_date

            if (
                closest_expiration_date > product_exp_date
                and today < product_exp_date
            ):
                closest_expiration_date = product_exp_date
                company_appears = cls.count_company_appears(
                    product["nome_da_empresa"], list
                )

            if company_appears > products_in_stock:
                bigger_stock_company = product["nome_da_empresa"]
                products_in_stock = company_appears

        message1 = (
            f"Data de fabricação mais antiga: {earliest_manufacturing_date}"
        )

        message2 = (
            f"Data de validade mais próxima: {closest_expiration_date}"
        )

        str_message3 = "Empresa com maior quantidade de produtos estocados: "

        message3 = (
            f"{str_message3}{bigger_stock_company}"
        )
        return f"{message1}\n{message2}\n{message3}"
