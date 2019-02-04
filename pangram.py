#Jjlijsdf;skdfg
import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
 
n=input()
if(ispangram(n)==True):
	print("yes")
else:
	print("no")
