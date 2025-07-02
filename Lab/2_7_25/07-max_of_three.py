# รับค่าจำนวนเต็ม 3 ค่า
a = int(input())
b = int(input())
c = int(input())

# หาค่ามากที่สุด
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
