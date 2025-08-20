n = int(input())

if 0 <= n <= 20:
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    print(str(n) + "! =", result)
else:
    print("error")