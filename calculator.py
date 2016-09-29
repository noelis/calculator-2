"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from sys import exc_info
from arithmetic import *


# Your code goes here
while True:
	try:
		user_request = raw_input(" >> ")
		if user_request == "quit" or user_request == "q":
			break
		elif len(user_request) <= 1 or user_request[0] == " ":
			print "Nice try! Please enter a valid number of inputs."	
		elif user_request[0:6] == "square" or user_request[0:4] == "cube":
			if user_request[6] == " " or user_request[4] == " ":
				tokens = user_request.split()
				operator,num1 = tokens
				num1 = int(num1)
				if operator == "square":
					print square(num1)	
				elif operator == "cube":
					print cube(num1)
			else:
				print "Invalid command! Make sure you check your spelling."
		else:
			tokens = user_request.split()
			operator,num1, num2 = tokens
			num1 = int(num1)
			num2 = int(num2)
			if operator == "+":
				print add(num1, num2)
			elif operator == "-":
				print subtract(num1, num2)
			elif operator == "*":
				print multiply(num1, num2)
			elif operator == "/":
				print divide(num1, num2)
			elif operator == "pow":
				print power(num1, num2)	
			elif operator == "mod":
				print mod(num1, num2)
			else:
				print "Invalid command! Please try again!"		
	except ValueError:
		print "Invalid command! Try again!"
	except:
		print "Goodbye ! Exiting the calculator !"
		break	
			
		