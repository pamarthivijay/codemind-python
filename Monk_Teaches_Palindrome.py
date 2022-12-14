a=int(input())
for i in range(a):
    l=input()
    x=l[::-1]
    if x==l:
        print("YES",end=" ")
        if len(l)%2==0:
            print("EVEN")
        else:
            print("ODD")
    else:
        print("NO")