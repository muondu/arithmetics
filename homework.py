a = input("""Hello.This is what I can do
1) to display even
2) to display odd
3) too display prime
If you want the computer to get for you one of those,please input here: 

""")
if a == "1":
	def even():
			input1 = int(input("Enter the number that you want the code to start from:  "))
			input2 = int(input("Enter the number that you want the code to end:  "))
		for a in range(input1,input2):
			if a % 2 == 0:
				print(a)
	even()
elif a == "2":
	def odd():
		a = int(input("Enter the number that you want the code to start from:  "))
		b = int(input("Enter the number that you want the code to end:  "))
		for c in range(a,b):
			if c % 2 != 0:
				print(c)
	odd()
elif a == "3":
	def prime():

		input3 = int(input("Enter your first number you want to begin with:  "))
		input4 = int(input("Enter your second number you want to end with:   "))
		for d in range(input3,input4):
			if d > 1:
				for e in range(2,d):
					if d % e == 0:
						break
				else:
					print(d)

			else:
				print("Your number is not found in the code")
				print(a)
	prime()