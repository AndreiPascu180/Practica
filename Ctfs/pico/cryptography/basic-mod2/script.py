#!/usr/bin/env python3
import string
import math

with open("message.txt") as fp:
	mesaj=fp.read()
	mesaj=mesaj.split()
	mesaj=[int(elem) for elem in mesaj]
	mesaj=list(map(lambda nr: pow(nr,-1,41),mesaj))

	print("picoCTF{",end="")

	for elem in mesaj:
		if elem in range(1,27):
			print(string.ascii_uppercase[elem-1],end="")
		elif elem in range(27,37):
			print(string.digits[elem-27],end="")
		else:
			print('_',end="")
	print("}")