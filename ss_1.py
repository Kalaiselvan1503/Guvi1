#dffgsd
a=[]
for z in range(int(input())):
    l=list(map(int,input().split()))
    for i in l:
        a.append(i)
a.sort()
print(*a)
