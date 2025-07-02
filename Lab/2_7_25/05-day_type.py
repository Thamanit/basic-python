# รับหมายเลขวันในสัปดาห์
day = int(input("Enter day (1-7): "))

# ตรวจสอบว่าเป็นวันหยุดหรือวันทำงาน
if 1 <= day <= 5:
    print("Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid day")  # เผื่อกรณีเลขผิด
