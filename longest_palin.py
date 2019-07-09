#ohishdiojg
s=input()
l=len(s)
c=[]
for i in range(0,l):
    for j in range(i+1,l):
        c.append(s[i:j+1])
max=1
d=[]
for i in c:
    if(i==i[::-1]):
        d.append(i)
d.sort(key=len)
d=d[::-1]
print(len(s)-len(d[0]))
