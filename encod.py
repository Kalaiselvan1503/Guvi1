#;kj;dj;zfg
s1=input()
s2=input()
li=[]
for i in range(0,len(s1)):
	o=ord(s1[i])-96+ord(s2[i])-96
	if o<26:
		s3=chr(o+96)
	else:
	    s3=chr(o-26+96)
	li.append(s3)
for i in li:
	print(i,end='')
