#njkjgikjipkdf
m,n=map(int,input().split())
c=m*n
li=[]
for i in range(1,9):
	d=i*i
	li.append(d)
	
if(c in li):
	print("yes")
else:
	print("no")
