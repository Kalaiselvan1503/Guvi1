#kalaisel
n=int(input())
l=len(str(abs(n)))
c=0
for i in range(n):
	d=n%10
	c=c+(d**l)
	n=n//10
print(c)
