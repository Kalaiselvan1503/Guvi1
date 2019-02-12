#jojpfjk;d
x,y =map(str,input().split())
c = 0
c+=abs(len(y)-len(x))
if(len(x)<=len(y)):
	max = y
	min = x
else:
	max = x
	min = y
for i in range(len(min)):
	if(min[i]!=max[i]):
		c+=1
print(c)
