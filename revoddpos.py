#hiojsldfjslj
g=input().split( )
li1=[]
for i in range(0,len(g)):
   if i%2!=0: 
      li1.append(g[i])
   else:
      a=g[i]
      b=a[::-1]
      li1.append(b)
      a=''
      b=''
print(*li1)
