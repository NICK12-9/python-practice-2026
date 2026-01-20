money_input = int(input('Здравствуйте, введите сумму в рублях (RUB): '))
currency = input("Спасибо! Введите валюту для конвертации (USD, EUR, CNY): ")

match currency:
    case 'USD':
        result = money_input / 90
    case 'EUR':
        result = money_input / 98
    case 'CNY':
        result = money_input / 12.5
    case _:
        print('Ошибка: неизвестная валюта')
        exit()

print(f"{money_input} RUB = {result:.2f} {currency}")