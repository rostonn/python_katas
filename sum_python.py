# recursive python function returns the sum of the first n integers

def python_sum(n):
	if n == 1:
		return 1
	else:
		return n + python_sum(n-1)

print(python_sum(3))
print(python_sum(4))
