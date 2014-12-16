import random
import math
import pylab 

def ransac(x, y, modelMethod, minSamples, inliersMethod, inliersDistanceThreshold, maxTrials = 1000, \
	   maxAttempts = 100, probabilityErrorFreeSelection  = 0.99, verbose = False, plot = False):
	"""
        	Using the RANdom SAmple Consensus (RANSAC) to implement this model fitting \
		   approach for an arbitrary set of data and a user-specified model. Also plot \
		   the points 
		Args:
			x [tuple]
			y [tuple]
			modelMethod [model parameters for a provided subset of the data, x and y]
			minSamples [minimum number of points]
			inliersMethod [ list when dependent variable falls within the distance threshold \
			   corresponding independent variable locations]
			inliersDistanceThreshold [ximum distance a data point may be located from the model]
			maxTrials [maximum number of iterations]
			maxAttempts[max attempts to fit model]
			probabilityErrorFreeSelection [.99]
			verbose [fasle]
			plot [false] 
		
		Return:
			tuple containing the model parameters or None if an adequate model was not found \
			   within the maximum number of trials permitted.
		Author:
			Lindsay Martinescu
        	"""
	iterations = 0
	maxIterations = float("inf")
	numberInliers = 0
	while maxIterations > iterations:
		if verbose == True:
			print 'Trial = ' + str((iterations + 1)) + '(of ' + str(maxIterations) + ' required)'
		modelDegenerate = True
		attempt = 0
		while modelDegenerate == True:
			attempt = attempt + 1
			if verbose == True:
				print '   Attempt = ' + str(attempt)
			topPoint = (len(x) - 1)
			indices = random.sample(range(len(x)), minSamples)
			xValues = []
			yValues = []
			for i in indices:
				xValues.append(x[i])
				yValues.append(y[i])
			modelParameters = modelMethod(xValues, yValues)
			if verbose == True:
				print '      Random indices = ' + str(indices)
				print '      Random x values = ' + str(xValues)
				print '      Random y values = ' + str(yValues)
				print '      Model parameters = ' + str(modelParameters)
			if modelParameters != None:
				modelDegenerate = False
		inliers = inliersMethod(modelParameters, x, y, inliersDistanceThreshold)
		if verbose == True:	
				print '      Inlier indices = ' + str(inliers)
		if len(inliers) > numberInliers:
			numberInliers = len(inliers)
			bestModel = modelParameters
			bestIndices = inliers
			percentInliers = numberInliers / float(len(x))
			maxIterations = (math.log((1 - probabilityErrorFreeSelection )) / math.log(1 - (percentInliers ** minSamples)))
			if verbose == True:
				print '         ****************** BETTER MODEL FOUND ****************'
				print '         Currently largest number of inliers found = ' + str(numberInliers)
				print '         Best inliers = ' + str(bestIndices)
				print '         Best parameters = ' + str(bestModel)
				print '         Proportion of inliers to total points = ' + str(percentInliers)
				print '         Revised number of trials required = ' + str(maxIterations)
				print '         ******************************************************'
		iterations = iterations + 1
		if iterations > maxTrials:
			raise "Past Maximum Iterations"
			return -1
	if plot == True:
		print 'Preparing inlier/outlier plot (close plot to continue) ...'
		goodX = []
		goodY = []
		x = tuple(x)
		y = tuple(y)
		badX = list(x)
		badY = list(y)
		for i in bestIndices:
			goodX.append(x[i])
			goodY.append(y[i])
			badX.remove(x[i])
			badY.remove(y[i])
		pylab.figure()
		pylab.xlabel('x')
		pylab.ylabel('y')
		pylab.xlim([min(x), max(x)])
		pylab.ylim([min(y), max(y)])
		pylab.plot(goodX, goodY, 'g.')
		pylab.plot(badX, badY, 'r.')
		pylab.show()

	return bestModel
if __name__ == "__main__":
    import math

    def linear(x, y):
        xysum = 0.0
        xsum = 0.0
        ysum = 0.0
        x2sum = 0.0
        
        for px,py in zip(x,y):
            xysum += px*py
            xsum += px
            ysum += py
            x2sum += px**2
        n = len(x)
        try:
            slope = (n*xysum - (xsum*ysum))/( (n*x2sum) - xsum**2)
            intercept = (ysum - slope * xsum)/n
            return (intercept,slope)
        except ZeroDivisionError:
            return None

    def linearInliers(modelParameters, x, y, distanceThreshold):
       	linePoint = modelParameters[0]
	slope = modelParameters[1]
	inliers = []
	for i in range(len(x)):
		xValue = x[i]
		yValue = y[i]
		distance = abs(yValue - (slope * xValue) - linePoint) / math.sqrt((slope ** 2) + 1)
		if distance < distanceThreshold:
			inliers.append(i)
	inliersTuple = tuple(inliers)
	return inliersTuple


    import statistics.model_fitting

    x = [0, 1, 2, 3, 3, 4, 10]
    y = [0, 1, 2, 2, 3, 4, 2]

    modelParameters = linear([x[4], x[3]], [y[4], y[3]])
    print '"linear" returned modelParameters =', modelParameters, '{should be None}'
    modelParameters = linear([x[6], x[1]], [y[6], y[1]])
    print '"linear" returned modelParameters =', modelParameters, '{should be (0.888888888, 0.111111111)}'
    modelParameters = linear([x[3], x[2]], [y[3], y[2]])
    print '"linear" returned modelParameters =', modelParameters, '{should be (2.0, 0.0)}'
    modelParameters = linear(x[0:2], y[0:2])
    print '"linear" returned modelParameters =', modelParameters, '{should be (0.0, 1.0)}'
    distanceThreshold = 0.1
    inlierIndices = linearInliers(modelParameters, x, y, distanceThreshold)
    print '"linearInliers" returned inlierIndices =', inlierIndices, '{should be (0, 1, 2, 4, 5)}'

    minSamples = 2
    modelParameters = statistics.model_fitting.ransac(x, 
                                                     y, 
                                                     linear, 
                                                     minSamples, 
                                                     linearInliers, 
                                                     distanceThreshold,
                                                     maxTrials=1000, 
                                                     maxAttempts=100, 
                                                     probabilityErrorFreeSelection =0.99,
                                                     verbose=True,
                                                     plot=True)
    print ''
    print '"ransac" returned modelParameters =', modelParameters, '{should be (0.0, 1.0)}'
