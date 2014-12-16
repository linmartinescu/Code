import random
import math

def monte_carlo_hit_or_miss (f, lowerLimit, upperLimit, acceptableError, maximumIterations = 100000, numberOfSamples = 1000):
    """
    Computes the area under the curve by creating a population and sample 
    Args:
        f = function
	lowerLimit = the lower (left-hand) boundary
	upperLimit = the upper (right-hand)
	acceptableError = the acceptable error for the approximation of the area
	maximumIterations = the maximum allowable number of iterations (defult 100000)
        numberSamples = the number of samples at which to define the function
    Return:
	Returns the area under the curve
    Author:
        Lindsay Martinescu
    """
    fxMax = 0.0
    points = []
    #f is function 
    # calculate a population of points
    for i in range(0,maximumIterations):
        xi = random.uniform(lowerLimit,upperLimit)  # get random value in range
        fxi = f(xi)         # calculate f(x)
        points.append(fxi)
    # now select k random samples of the points
    kpoints = random.sample(points,numberOfSamples);
    # get the max value from the sample
    fxMax = max(kpoints)    
    
    # now we can loop through our iterations, and count hits/misses
    h = 0               # initialize hit count
    n = 0               # initialize iteration count
    for i in range(0,numberOfSamples-1):
        n = n+1                         #increment iteration count
        xi = random.uniform(0.0,fxMax)  # get random value in range [0,fxMax]
        if (xi <= kpoints[i]):          # see if the point is <= f(xi) where i in [0,k-1]
            h = h+1                         #  increment hit count
        # now, calculate area
        hn = float(h)/float(n)
        area = hn * (upperLimit - lowerLimit) * fxMax
        # and calculate error
        error = (2.0/3.0)*(upperLimit-lowerLimit)* fxMax * math.sqrt((hn*(1.0 - hn))/n)
        if (n > 10 and error < acceptableError):
            break
    return area