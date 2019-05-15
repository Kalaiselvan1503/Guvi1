#opjijfg
n=int(input())
s=str(n)
li=[]
l=[]
for i in s:
  li.append(i)
for i,j in enumerate(li):
  if i%2!=0:
    l.append(j)
print(*l)
