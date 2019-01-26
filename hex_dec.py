#jhgkjj
import string
s = input()
if (s==(all(c in string.hexdigits for c in s))):
	print("no")
else:
	print("yes")
