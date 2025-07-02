# รับจำนวนเต็มจากผู้ใช้
num = int(input("Enter a number: "))

# ตรวจสอบว่าเป็นบวก ลบ หรือศูนย์
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
