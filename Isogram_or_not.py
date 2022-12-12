a=input()
b=a.lower()
c=set(b)
d=[]
for i in b:
    if b.count(i)==1:
        d.append(i)
if len(c)==len(d):
    print(True)
else:
    print(False)