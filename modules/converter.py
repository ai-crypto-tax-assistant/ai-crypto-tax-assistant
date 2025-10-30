class Converter:
    def __init__(self, fiat_currency="USD"):
        self.fiat = fiat_currency

    def convert(self, transactions):
        # TODO: Конвертировать крипту в фиат по дате транзакции
        print(f"Converting all transactions to {self.fiat}...")
        for tx in transactions:
            tx["fiat_value"] = 100  # заглушка
        return transactions
