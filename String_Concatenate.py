a=input()
b=list(a)
x=input()
y=list(x)
res=b+y
res.sort()
for i in res:
    print(i,end="")