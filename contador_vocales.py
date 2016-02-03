contador = 0
s = "azcbobobegghauuil"
for letra in s:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        contador += 1
    
print "Number of vowels", contador