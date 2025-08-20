def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

while True:
    x = int(input())
    if x == 0:
        break
    if is_prime(x):
        print(f"{x}: prime")
    else:
        print(f"{x}: not prime")