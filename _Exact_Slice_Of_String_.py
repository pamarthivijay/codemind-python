a=input()
b=list(a)
l=[]
x=int(input())
y=int(input())
for i in range(len(b)):
    if i>=x and i<=y:
        l.append(b[i])
for i in l:
    print(i,end="")