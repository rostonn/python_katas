x = float(input("1st Number: "))
y = float(input("2nd number: "))
z = float(input("3rd number: "))

if x > y and x > z:
	maximum = x
elif y > x and y > z:
	maximum = y
else:
	maximum = z

print("the maximal value is: "+str(maximum))
