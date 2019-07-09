#knjkdjgk
k,s=map(str,input().split())
l=0
if len(k)>len(s):
  k,s=s,k
i=0
while i<len(k):
  l+=(ord(s[i])-ord(k[i]))
  i+=1
for i in range(i,len(s)):
  l+=ord(s[i])-ord('a')+1
print(l)
