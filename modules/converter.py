class Converter:
    def __init__(self, fiat_currency="USD"):
        self.fiat = fiat_currency

    def convert(self, transactions):
        # TODO: Convert all crypto transactions to fiat based on transaction date
        print(f"Converting all transactions to {self.fiat}...")
        for tx in transactions:
            tx["fiat_value"] = 100  # Placeholder
        return transactions
