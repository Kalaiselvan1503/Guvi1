#jjgsg
s=0
k=0
l=[]
v=input()
for i in v:
  if i not in l:
    l.append(i)
    k+=1
    if s<k:
       s=k
  else:
    k=0
print(s)    
