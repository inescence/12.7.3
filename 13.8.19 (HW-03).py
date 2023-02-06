tickets = int(input("Введите количество билетов"))
users = tickets

sum=0
while tickets !=0:
    age = int(input("Введите возраст участника"))
    if 0 <= age < 18:
        print('ticket free')
    elif 18 <= age < 25:
        sum +=990
        print('Costs 990')
    elif 25 <= age <= 100:
        sum +=1390
        print('Costs 1390')
    else:
        print('некорректные данные')
        continue
    tickets -=1

if users > 3:
    sale = sum - (sum*10/100)
    print(f'Сумма к оплате:  {sale} руб., с учетом скидки 10%')
else:
    print(f'Сумма к оплате:  {sum} руб.')
