#jdsiojgo
s=input()
li=[]
for i in range(0,len(s)):
    li.append(ord(s[i]))
li.sort()
for i in li:
    print(chr(i),end='')
