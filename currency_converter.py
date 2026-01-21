import json
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

exchange_currency = {
    'USD': 90,
    'EUR': 98,
    'CNY': 12.5
}

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