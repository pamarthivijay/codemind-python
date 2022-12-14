a=input()
b=a.lower()
l=list(b)
x=input()
y=x.lower()
c=0
for i in l:
    if i==y:
        c+=1
if c>0:
    print(c)
else:
    print("-1")