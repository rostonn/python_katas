# Calculate the average of a variable number of arguments

def avg(*args):
    print(len(args))
    sum = 0
    for value in range(len(args)):
        sum += args[value]
    print(sum)
    return sum/(len(args))

ans = avg(1,2,3,4)
print(ans)
