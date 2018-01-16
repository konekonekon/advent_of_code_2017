# def add(x):
# 	def g(y):
# 		return x+y
# 	return g


# add3 = add(3)
# print(add3(5))


import functools


def doubled(f):
	@functools.wraps(f)
	def call(s):
		f(s)
		f(s)
	return call


def hello(name):
	print('Hello %s!' % name)


hheelllloo = doubled(hello)
hheelllloo('world')
hheelllloo('Ayano')


@doubled
@doubled
def bye(name):
	print("Bye %s!" % name)

bye('world')