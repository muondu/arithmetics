def code():
	a = int(input("""Hello.This is what I can do
	1) to display even
	2) to display odd
	3) too display prime
	If you want the computer to get for you one of those,please input here: 

	"""))
	input1 = int(input("Enter the number that you want the code to start from:  "))
	input2 = int(input("Enter the number that you want the code to end:  "))


	if a == 1:
		for a in range(input1,input2):
			if a % 2 == 0:
				print(a)


	elif a == 2:
		for c in range(input1,input2):
			if c % 2 != 0:
				print(c)




	elif a == 3:
		for d in range(input1,input2):
			if d > 1:
				for e in range(2,d):
					if d % e == 0:
						break
				else:
					print(d)




code()