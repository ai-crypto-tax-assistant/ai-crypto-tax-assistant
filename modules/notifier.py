class Notifier:
    def __init__(self, email):
        self.email = email

    def send_summary(self, tax_results):
        # TODO: Implement email or SMS notifications
        print(f"Sending tax summary to {self.email}...")
