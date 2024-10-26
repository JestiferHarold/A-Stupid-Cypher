from platform import system
from string import *
from utils import *
from array import *
name = system()
print(name)
tters = [ascii_letters]
auto = [digits]
anoter = [punctuation]
au = [f for x in auto for f in x]
le = [m for x in tters for m in x]
an = [d for x in anoter for d in x]
le.extend(au)
le.extend(an)

m = le[-1]
del le[-1],au,tters,auto

l = dict.fromkeys(le,1)
l['~'] = -1

le.append(m)
f = {x: set() for x in le}

k = [x for x in input("Enter some words   ")]
m = ''
s = list(k)
for i in k:
    q = 0
    k = list(s)
    v = k.count(i)
    if not i.isspace():
        for a in range(v):
            f[i].add(k.index(i) + q)
            del k[k.index(i)]
            q += 1


for i in k:
    if i.isspace(): 
        m += ' '
        continue
    if l[i] +1 == 94:
        l[i] = 0    
    if l[i] + le.index(i) + 1 == 94 or i == "~":
        d = 0
        m = m + le[l[i] + 1]
        l[i] += 1
    else:
        l[i] = 0 if l[i]-1 > len(le) else l[i]
        r = le.index(i)
        m = m + le[l[i] + r]
        l[i] += 1

file = f"files/encrypted/{input("Enter the name of the encrypted file : ")}.txt" if name in "Linux" else f"files\\encrypted\\{input("Enter the name of the encrypted file : ")}.txt"

with open(file, 'w') as g:
    g.write(m)

print("The encrypted text is  ", m)
