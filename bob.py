numBobs = 0
s = 'azcbobobegghakl'
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print 'Numero de veces que aparece bob:', numBobs