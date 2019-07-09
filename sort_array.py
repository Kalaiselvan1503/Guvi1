#arrayydg
s,k=map(int,input().split())
if s>k:
    s,k=k,s
li=[]
for i in range(s):
    m=list(map(int,input().split()))
    m.sort()
    li.append(m)
for j in range(0,k):
    li1=[]
    for i in range(0,s):
        li1.append(li[i][j])
    li1.sort()
    r=0
    for i in range(0,s):
        li[i][j]=li1[r]
        r=r+1
for i in li:
    print(*i)
