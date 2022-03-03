a = input("Как тебя зовут? ")
b = int(input("Сколько тебе лет? "))
if b > 9:
    c = b // 10 + b % 10
    d = (b // 10) * (b % 10)
else:
    c = b
    d = b
print(len(a), c, d)