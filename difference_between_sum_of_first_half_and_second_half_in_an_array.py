a=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
b=len(l)//2
for i in range(b):
    x.append(l[i])
for j in range(b,len(l)):
    y.append(l[j])
q=(sum(x))
w=(sum(y))
m=q-w
if m>0:
    print(m)
else:
    print(-m)