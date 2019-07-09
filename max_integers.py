#kbjksd
p,s,o,f=map(int,input().split())
nm=[int(i) for i in input().split()]
q=[s*nm[i]+o*nm[j]+f*nm[k]
for i in range(len(nm)) 
for j in range(len(nm))
for k in range(len(nm)) 
if i<=j<=k]
print(max(q))
