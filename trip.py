#sgfbh
n=int(input())
d=list(map(int,input().split()))
c=0
for i in range(0,n-2):
  for j in range(i+1,n-1):
    for k in range(j+1,n):
      if d[i]<d[j]<d[k]:
        c+=1
print(c)        
