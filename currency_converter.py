continue_choice = 'y'

history =[]
while True:
    if continue_choice == 'y':
        money_input = int(input('Здравствуйте, введите сумму в рублях (RUB): '))
        currency = input("Спасибо! Введите валюту для конвертации (USD, EUR, CNY): ").upper()
        match currency:
            case 'USD':
                result = money_input / 90
                print(f"{money_input} RUB = {result:.2f} {currency}")
                history.append({
                    'amount_rub': money_input,
                    'cur': currency,
                    'result': result
                })
                continue_choice = input('Хотите продолжить? Если да введите \'y\' иначе \'n\': ')
            case 'EUR':
                result = money_input / 98
                print(f"{money_input} RUB = {result:.2f} {currency}")
                history.append({
                    'amount_rub': money_input,
                    'cur': currency,
                    'result': result
                })
                continue_choice = input('Хотите продолжить? Если да введите \'y\' иначе \'n\': ')
            case 'CNY':
                result = money_input / 12.5
                print(f"{money_input} RUB = {result:.2f} {currency}")
                history.append({
                    'amount_rub': money_input,
                    'cur': currency,
                    'result': result
                })
                continue_choice = input('Хотите продолжить? Если да введите \'y\' иначе \'n\': ')
            case _:
                print('Ошибка: неизвестная валюта')
                print("Повторите попытку")
                continue
    else:
        break

print(f'История конвертаций:')
for i in history:
    print(f"{i['amount_rub']} RUB = {i['result']:.2f} {i['cur']}")

