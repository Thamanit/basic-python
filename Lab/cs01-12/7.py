num = int(input('enter your loop'))
numtotal = []
for i in range(num):
    data = int(input('enter your data:'))
    numtotal += [data]
print(numtotal)
numtotal.sort()
print(numtotal)