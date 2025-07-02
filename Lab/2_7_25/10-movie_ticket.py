# รับอายุและวันในสัปดาห์
age = int(input())
day = int(input())

# คำนวณราคาตั๋วตามอายุ
if age < 13:
    price = 100
elif age <= 60:
    price = 180
else:
    price = 120

# เพิ่มราคาวันหยุด
if day == 6 or day == 7:
    price += 50

print(price)
