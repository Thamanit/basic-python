# รับจำนวนเต็มจากผู้ใช้
number = int(input("Enter a number: "))

# ตรวจสอบว่าเป็นเลขคู่หรือเลขคี่
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
