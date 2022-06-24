#!/usr/bin/env python3

with open("message.txt") as fp:
	content=fp.read()

print(content)

limit = len(content)-2
i=0
while i < limit:
	a=content[i]
	b=content[i+1]
	c=content[i+2]
	print(c+a+b,end="")
	i+=3
