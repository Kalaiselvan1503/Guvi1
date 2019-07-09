#ijjdgosg
n=input()
k=0
for i in range(0,len(n)-1):
  for j in range(i+1,len(n)):
    if n[i]<n[j]:
      k=1
      print(n[j:])
      break
  if k==1:
    break
  else:
      print(n)
