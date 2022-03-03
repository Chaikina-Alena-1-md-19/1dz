a = input("Как тебя зовут? ")
a1 = a.upper()
a2 = a.lower()
s = a[1:]
s1 = a[:1]
a3 = s1.upper() + s.lower()
a4 = s1.lower() + s.upper()
print(a1,a2,a3,a4)