def square(n):
	# a=n*n
	# print(a)
	# return n*n
	for i in range(5):
		print(i+n)
		for j in range(7):
			print(n*n)
	return n*n*n
square(4)
square(5)
square(13)
x=square(13) #this also runs square(), aka everything inside. Runs it first, then assigns
print(x)