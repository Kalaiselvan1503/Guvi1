#jnklflkg
s=input().split()
li=[]
for i in range(0,len(s)):
	a=s[i][::-1]
	li.append(a)
print(*li)
