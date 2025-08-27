s = input()
i = 0
while i < len(s) and (s[i].isdigit() or s[i]=='.'):
    i += 1
num = float(s[:i])
word = s[i:]
print(f"In {int(num)//10} years I have spotted {num%10} {word}.")