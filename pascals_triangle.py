# Pascal's Triangle

#First and last numbers are always 1
#Second number is n-1 + 1
ans = []
def pascal(n):
	if n == 1:
		ans.append([1])
		return [1]
	else:
		line = [1]
		previous_line = pascal(n-1)
		for i in range(len(previous_line)-1):
			line.append(previous_line[i] + previous_line[i+1])
		line += [1]
		ans.append(line)
	return line

test = pascal(15)

print(ans)
max_width = len(str(max(ans[len(ans)-1])))
print(max_width)
last_string = ''
for c in ans[len(ans)-1]:
	last_string += str(c)+2*' '
length = len(last_string)
print(length)

for i in range(len(ans)):
	string = ''
	# if i == 0:
	#
	# else:
	# 	pl = len(ans[i-1])+2
	for j in range(len(ans[i])):
		padding = max_width - len(str(ans[i][j]))
		string += padding*' '+str(ans[i][j])+' '
	print(string.center(length,' '))
