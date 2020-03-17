def find_even():
	input1 = int(input("Enter the number that you want the code to start from:  "))
	input2 = int(input("Enter the number that you want the code to end:  "))
	for a in range(input1,input2):
		if a % 2 == 0:
			print(a)
find_even()