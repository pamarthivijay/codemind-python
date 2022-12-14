n=input()
m=n.lower()
l=list(m)
vow="aeiou"
dig="0123456789"
v=[]
c=[]
d=[]
s=[]
for i in l:
    if i in vow:
        v.append(i)
    if i!=" " and i not in vow and i not in dig:
        c.append(i)
    if i in dig:
        d.append(i)
    if i==" ":
        s.append(i)
print("Vowels:",len(v))
print("Consonants:",len(c))
print("Digits:",len(d))
print("White spaces:",len(s))