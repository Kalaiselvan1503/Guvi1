#kjkkdsjgf
import math
m,n=map(int,input().split())
l=[]
j=math.gcd(m,n)
l.append(j)
for p in range(0,len(l)):
  if(p==len(l)-1):
    print(l[p],end="")
  else:
    print(l[p],end=" ")
