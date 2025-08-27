a = input()
b = input()
if a.lower() < b.lower():
    print("A comes before B")
elif a.lower() > b.lower():
    print("A comes after B")
else:
    print("A equals B")