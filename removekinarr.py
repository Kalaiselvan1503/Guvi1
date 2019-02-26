#shdjfghksjk
n,f=map(int,input().split( ))
c=list(map(int,input().split( )))
for i in range(0,n):
	if f in c:
		c.remove(f)
if len(c)==0:
	print("empty")
else:
	print(c)	
