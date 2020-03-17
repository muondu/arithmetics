def odd():
	a = int(input("Enter your first number:  "))
	b = int(input("Enter your second number:  "))
	for c in range(a,b):
			if c % 2 != 0:
				print(c)
odd()