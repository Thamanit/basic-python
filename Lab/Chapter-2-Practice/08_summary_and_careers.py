# รับข้อมูลจากผู้ใช้
bill, tip_percent, people = input().split()
bill = float(bill)
tip_percent = float(tip_percent)
people = int(people)

# คำนวณค่าทิปและยอดต่อคน
tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount
per_person = total / people

# แสดงผลลัพธ์
print(f"Each person pays: {round(per_person, 2)}")

# คอมเมนต์อาชีพที่เกี่ยวข้อง
# นักพัฒนา Python สามารถทำงานในสาขา Web Development, Data Science, AI, และ Cybersecurity ได้