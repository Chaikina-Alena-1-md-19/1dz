a = input("Как тебя зовут? ")
b = int(input("Сколько тебе лет? "))
if a.isalpha() == True and " " not in a:
    print("имя верно введено")
else:
    print("имя не верно введено")
if b >= 0 and b < 150:
    print("число верно введено")
else:
    print("число не верно введено")
