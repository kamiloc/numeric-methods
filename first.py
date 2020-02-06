# Import modules example
from math import *

# Define a variable
num = 4
great = "Hello world !"

# Define a function
def elevate(arg, exp): 
	return arg**exp

# Using math library in a function
def square(num):
	return sqrt(num)

# Testing functions/variables tough a print
# print(great)
# print(elevate(num,3))
# print(square(25))

# Testing a loop
i, firstArr = 0, [3, 2, 4, 7, 9, 0, 2, 1]
while i < len(firstArr):
	print("Position: " + str(i) + " is : " + str(firstArr[i]))
	i = i + 1

# Create a factorial function
def factorial(num):
	if num == 0: 
		return 1
	else: 
		return num * factorial(num - 1) 

print(factorial(3))