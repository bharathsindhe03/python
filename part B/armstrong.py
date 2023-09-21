def isArmstrong(x):
	n = 0
	temp = x
	x1=x
	while (x!=0):
		n = n + 1
		x = x // 10
	sum1 = 0
	while (temp != 0):
		r = temp % 10
		sum1 = sum1 + (r**n)
		temp = temp // 10
	return (sum1 == x1)

x = 153
print(isArmstrong(x))

x = 1253
print(isArmstrong(x))
