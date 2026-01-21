import json
import requests
def get_exchange_rates():
    try:
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        response.raise_for_status()
        data = response.json()
        rates = {}
        if 'Valute' in data:
            for code, info in data['Valute'].items():
                rates[code]=info['Value']
        return rates
    except Exception as e:
        print(f"Не удалось загрузить курсы. Использую резервные значения.")
        return {'USD': 90, 'EUR': 98, 'CNY': 12.5}

history =[]
try:
    with open('history.json', 'r') as file:
        data = json.load(file)
        if isinstance(data, list):
            history = data
        else:
            history = []
except (FileNotFoundError, json.JSONDecodeError, ValueError):
    history = []

exchange_currency = get_exchange_rates()
supported_currencies = {'USD', 'EUR', 'CNY'}
exchange_currency = {k: v for k,v in exchange_currency.items() if k in supported_currencies}

def save_history():
    with open('history.json', 'w') as file:
        json.dump(history, file, indent=2)

while True:
    try:
        money_input = int(input('Здравствуйте, введите сумму в рублях (RUB): '))
    except ValueError:
        print("Ошибка введите целое число")
        continue
    if money_input <= 0:
        print("Сумма должна быть больше 0")
        continue
    currency = input("Спасибо! Введите валюту для конвертации (USD, EUR, CNY): ").upper()
    if currency not in exchange_currency:
        print("Данная валюта не поддерживается, попробуйте еще раз)")
        continue
    rate_of_currency = exchange_currency[currency]
    result = money_input / rate_of_currency
    print(f"{money_input} RUB = {result:.2f} {currency}")
    history.append({
        'amount_rub': money_input,
        'cur': currency,
        'result': result
    })
    save_history()
    continue_choice = input("Хотите продолжить? Если да введите \'y\' иначе \'n\': ").lower()
    if continue_choice != 'y':
        break

print(f'История конвертаций:')
for i in history:
    print(f"{i['amount_rub']} RUB = {i['result']:.2f} {i['cur']}")