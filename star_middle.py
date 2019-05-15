#hdjgo
a=input()
c=list(a)
b=len(c)
f=0
if b%2==0:
	i=b//2
	c[i]='*'
	c[i-1]='*'
	t=''.join(c)
	print(t)
else:
	f=b//2
	c[f]='*'
	e=''.join(c)
	print(e)
