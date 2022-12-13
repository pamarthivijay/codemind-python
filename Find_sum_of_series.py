n=int(input())
l=[]
for i in range(1,n+1):
    a=1/i
    l.append(a)
b=sum(l)
print("%0.2f"%b)