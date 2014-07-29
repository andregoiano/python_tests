import math, cmath

def calc(number):
	return number * math.cos(number)

def calc2(number):
	a = number + 3
	b = a + math.cos(number)
	return b

print calc(20)
print calc2(20)