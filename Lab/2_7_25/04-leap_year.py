# รับปี ค.ศ. จากผู้ใช้
year = int(input("Enter year: "))

# ตรวจสอบว่าเป็นปีอธิกสุรทินหรือไม่
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
