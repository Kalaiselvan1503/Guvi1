#jhjisjgf
n=int(input())
l=[list(map(int,input().split(" "))) for i in range(n)]
s=0
for i in range(n):
	s=s+l[i][i]
print(s)
