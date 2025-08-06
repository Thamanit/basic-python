n = int(input())
between = []
for _ in range(n):
    num = int(input())
    if 10 <= num <= 50:
        between.append(num)
print("ค่าที่อยู่ในช่วง 10-50:", between)