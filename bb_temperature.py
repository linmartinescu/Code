from Blackbody import Blackbody

def bb_temperature(wavelength, radiance, epsilon = 1e-8):
	tLow = 0.0	# initial low temperature
	tHigh = 6000.0	# initial high temperature
	tResult = (tHigh + tLow)/2.0	# current calculated temperature
	while ((tHigh - tLow) > epsilon):	# while our temperature difference is > epsilon, loop
		tBb = Blackbody(wavelength, tResult)	#create a new blackbody for the given wavelength and current temperature
		cRadiance = tBb.radiance()		#calculate current radiance
		if (cRadiance > radiance):		# if calculated radiance is > target radiance, set new 'high'
			tHigh = tResult
		else:					# else , set new 'low'
			tLow = tResult
		tResult = (tHigh + tLow)/2.0		# compute new target temperature, continue loop

	return tResult

	def spectral_radiance(self, wavelengths):
		"""
                Computes a list 

                Args:
                         wavelength in microns
                Returns:
                        the radiances
                Author:
                        Lindsay Martinescu
                """
		radiances = []
                for wavelength in wavelengths:
                        self.wavelength = wavelength
                        radiances.append(self.radiance())
                return radiances
	

if __name__ == '__main__':

	bb = Blackbody(10, 300)
	print bb
	print 'L =', bb.radiance(), '[W / m^2 / micron / sr]'
	print 'Peak wavelength =', bb.peak_wavelength(), '[microns]'

	import pylab

	pylab.figure()
	pylab.title('f(x) = sqrt(x)')
	pylab.xlabel('Wavelength [microns]')
	pylab.ylabel('Radiance [W / m^2 / micron / sr]')
	pylab.xlim([0,20])
	pylab.ylim([0,5])
	pylab.plot(x, y)
	pylab.show()
	
	n = 100
	x = []
	y = []
	xMin = 8
	xMax = 14
	increment = (xMax - xMin)/float(n)
	for i in range(n):
		x.append(xMin + i*increment)
	y = spectral_radiance(x)
