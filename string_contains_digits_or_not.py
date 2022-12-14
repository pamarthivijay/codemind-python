a=int(input())
for i in range(a):
    l1=0
    l=input()
    x=list(l)
    z="0123456789"
    for i in x:
        if i in z:
            l1+=1
    if l1!=0:
        print("Yes")
    else:
        print("No")