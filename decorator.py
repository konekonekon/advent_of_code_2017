import functools
import math


def trace(f):
	@functools.wraps(f)
	def called(p):
		print(f.__name__ + "(" + str(p) +  ") = " + str(f(p)))
		# return f.__name__ + "(" + str(p) +  ") = " + str(f(p))
		# return f(p)
	return called


@trace
def call(s):
	return s


@trace
def fact(n):
	# return product(range(1, n+1))
	return math.factorial(n)


call("I called trace")
fact(3)
fact(4)

# Sortie attendue:
# fact(3) = 6
# fact(4) = 24
