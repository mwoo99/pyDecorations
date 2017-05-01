import time

def printArg(func):
	def printFunc(*arg):
		print func.__name__ + ": " + str(arg)
	return printFunc

def timer(func):
	def inner2(*arg):
		start = time.time()
		result = func(*arg) 
		end = time.time()
		print "Execution time:" + str(end -start)
		return result
	return inner2

@timer
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

@printArg
def test(a,b,c):
	return "weeb"

test("i","got","mon$y")
fib(3)
