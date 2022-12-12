a=input()
b=input()
x=a.lower()
y=b.lower()
if x==y:
    print(False)
c=set(x)
d=set(y)
if c==d:
    print(True)
else:
    print(False)