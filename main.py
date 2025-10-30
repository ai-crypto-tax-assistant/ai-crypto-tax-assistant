from modules.importer import Importer
from modules.converter import Converter
from modules.calculator import Calculator
from modules.reporter import Reporter
from modules.notifier import Notifier
import json

# Загрузка конфигурации
with open("config.json") as f:
    config = json.load(f)

# 1. Импорт транзакций
importer = Importer(config)
transactions = importer.fetch_all()

# 2. Конвертация в фиат
converter = Converter(config["fiat_currency"])
transactions_fiat = converter.convert(transactions)

# 3. Расчет налогов
calculator = Calculator(config["jurisdiction"])
tax_results = calculator.calculate(transactions_fiat)

# 4. Генерация отчетов
reporter = Reporter()
reporter.generate_pdf(tax_results, "reports/tax_report.pdf")
reporter.generate_csv(tax_results, "reports/tax_report.csv")

# 5. Уведомления
notifier = Notifier(config["notify_email"])
notifier.send_summary(tax_results)

print("✅ Crypto Tax Assistant completed successfully!")
