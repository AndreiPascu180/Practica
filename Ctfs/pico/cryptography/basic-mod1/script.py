#!/usr/bin/env python3
import string

with open("message.txt") as fp:
	mesaj=fp.read()
	mesaj=mesaj.split()
	mesaj=[int(elem) for elem in mesaj]
	mesaj=list(map(lambda nr: nr%37,mesaj))

	print("picoCTF{",end="")

	for elem in mesaj:
		if elem in range(26):
			print(string.ascii_uppercase[elem],end="")
		elif elem in range(26,36):
			print(string.digits[elem-26],end="")
		else:
			print('_',end="")
	print("}")