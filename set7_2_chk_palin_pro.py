#iujhuisdhugvdj
a=input()
b,m='',0
for i in range(0,len(a)-1):
  for j in range(i,len(a)):
    b = b+a[j]
    if len(b)>1 and b == b[::-1]:
      if len(b)>m:
        m = len(b)
  b=''
print(len(a)-m)
