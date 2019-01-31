#huhhfdl
n=int(input())
l=[int(x) for x in input().split()]
k=[]
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            if l[i] in k:
                k.remove(l[i])
            else:k.append(l[i])

for i in range(0,len(k)):
    if i<len(k)-1:
        d=' '
    else:d=''
    print(k[i],end=d)
