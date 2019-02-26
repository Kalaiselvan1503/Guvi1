#IRTOOEJYIw454w
n1=int(input())
d=list(map(int,input().split( )))
s=k=0
for i in range(0,len(d)):
    if i%2==0:
        s=s+d[i]
    else:
        k=k+d[i]
if s>k:
    print(s)
else:
    print(k)
