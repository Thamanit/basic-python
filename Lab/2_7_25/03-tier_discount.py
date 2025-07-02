# รับยอดซื้อจากผู้ใช้
amount = float(input("Enter total amount: "))

# คำนวณส่วนลดตามระดับ
if amount >= 2000:
    discount = amount * 0.15
elif amount >= 1000:
    discount = amount * 0.10
elif amount >= 500:
    discount = amount * 0.05
else:
    discount = 0

# คำนวณราคาหลังหักส่วนลด
net_price = amount - discount
print(net_price)
