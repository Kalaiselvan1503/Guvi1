#dfgsg
import math
n,m=map(int,input().split())
c=math.log(n)
d=math.log(m)
e=c-d
f=math.exp(e)
if(f<1):
	print(0)
else:
	print(round(f))
