import random
import math

def monte_carlo_average(f, lowerLimit, upperLimit, acceptableError, maximumIterations = 100000):
	`"""
	Computes the average area
	Args:
		f = function
		lowerLimit = the lower (left-hand) boundary
		upperLimit = the upper (right-hand)
		acceptableError = the acceptable error for the approximation of the area
		maximumIterations = the maximum allowable number of iterations (defult 100000)
	Return:
		Returns the area under the curve
	Author:
            Lindsay Martinescu
	"""
	sum = 0.0   				# initialize our sum
	sumOfSquare = 0.0			# and the sum of squares (for error calculation)
	area = 0.0				# initialize our area
	n = 0					# initialize our count of iterations
	for x in range(0,maximumIterations):	# setup a loop, up to maximumIterations times
		n += 1
		xprime = random.uniform(lowerLimit, upperLimit)		# grab a random number in our range
		val = f(xprime)			# invoke our function on the random number and store value
		valSquare = (val*val)
		sum += val			# add it to current sum
		sumOfSquare += valSquare	# add the square of value to sumSquare, so we can calculate error
		f2 = sumOfSquare/n		# current value of f2, for error calculation
		fbar = sum/n			# fbar sum of f(xprime) / N 
		area = (upperLimit - lowerLimit) * fbar	# area == (upper - lower) * fbar
		fbarSquared = (fbar * fbar)	# fbar^2
		tmp = (f2 - fbarSquared)/n	# f2 - fbar^2 / n
		error = (upperLimit - lowerLimit) * math.sqrt(tmp) # full error calculation
		if (n > 2 and error < acceptableError):	# is our answer within acceptable error range?
			break
	return area;


