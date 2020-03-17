def prime():
	input1 = int(input("Enter your first number you want to begin with:  "))
	input2 = int(input("Enter your second number you want to end with:   "))
	for a in range(input1,input2):
		if a > 1:
			for b in range(2.0,a):
				if a % b == 0:
					break
			else:
				print(a)
prime()