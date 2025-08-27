line = input()
at = line.find('@')
sp = line.find(' ', at)
print(line[at+1:sp])