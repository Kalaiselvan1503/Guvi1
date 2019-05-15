#okijkidjfgjsxg
n=input()
c=0
for i in range(0,len(n)):
	if (n[i]=='0' or n[i]=='1'):
		c=c+0
	else:
		c=c+1
if (c==0):
	print("yes")
else:
	print("no")
