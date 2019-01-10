#kjsja;d
n=int(input())
c=0
for i in range(n):
	d=n%10
	c=c+(d*d)
	n=n//10
print(c)
