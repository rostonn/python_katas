import sys

text = ""
while True:
	c = sys.stdin.read(1)
	text = text + c
	if c == '\n':
		break

print("Input: %s" % text)
