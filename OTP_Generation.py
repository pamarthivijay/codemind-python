n=input()
l=list(n)
l1=[]
for i in l:
    a=int(i)
    if a%2!=0:
        b=a*a
        l1.append(b)
for i in l1:
    print(i,end="")