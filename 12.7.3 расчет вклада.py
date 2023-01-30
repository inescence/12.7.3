per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада"))
deposit = []
deposit.append(int(money * 5.6/100))
deposit.append(int(money * 5.9/100))
deposit.append(int(money * 4.28/100))
deposit.append(int(money * 4.0/100))
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))