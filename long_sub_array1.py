#hihdigj\
m=int(input())
n=list(map(int,input().split()))
o=[]
p=1
for i in n:
  if i not in o:
    o.append(i)
for i in range(len(o)-1):
  if (o[i]<o[i+1]):
    p+=1
print(p-1)
