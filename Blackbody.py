"""
    Aurthor: Lindsay Martinescu
"""

import math

class Blackbody(object):

        def __init__(self, wavelength, temperature):
                """
                Initializes the object

                Args:
                         wavelength in microns
                         temperature in Kelvin
                Author:
                        Lindsay Martinescu
		"""

                self.wavelength = wavelength 
                self.temperature = temperature

        def radiance(self):
                """
                Computes the radiance of a blackbody

                Args:
                         wavelength in microns
                         temperature in Kelvin
                Returns:
                        the radiance for a blackbody with the given temperature and wavelength
                Author:
                        Lindsay Martinescu
                """

                c1 = 3.74151e8
                c2 = 1.43879e4
                return c1 / ((math.pi*(self.wavelength**5)) * (math.exp(c2/(self.wavelength*self.temperature))-1));

        def peak_wavelength(self):
                """
                Compute the peak wavelength

                Args:
                        temperature in Kelvin

                Returns:
                        the peak wavelength for a blackbody with the given temperature

                Author:
                        Lindsay Martinescu
                """

                b = 2.897768551e3
                return b / self.temperature

        def __str__(self):
                return '[ temperature=' + str(self.temperature) +", wavelength=" + str(self.wavelength) + ' ]';
                """
                Prints a prettier version of self

                Returns:
                        a more easily read version of self
                Author:
                        Lindsay Martinescu
		"""
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

def bb_temperature(wavelength, radiance, epsilon = 1e-8):
        """
        Computes the temperture for a give radiance using a binary search 

        Args:
		wavelength in microns
                radiance in W / m^2 / sr / micron
		epsilon in K
	Returns:
                the temperture for a blackbody at a given radiance using a binary search 
        Author:
                Lindsay Martinescu
	"""

        tLow = 0.0	
        tHigh = 6000.0	
        tResult = (tHigh + tLow)/2.0
        while ((tHigh - tLow) > epsilon):	
                tBb = Blackbody(wavelength, tResult)
                cRadiance = tBb.radiance()
                if (cRadiance > radiance):
                        tHigh = tResult
                else:
                        tLow = tResult
                tResult = (tHigh + tLow)/2.0

        return tResult
	

	
if __name__ == '__main__':

	bb = Blackbody(10, 300)
	print bb
	print 'L =', bb.radiance(), '[W / m^2 / micron / sr]'
	print 'Peak wavelength =', bb.peak_wavelength(), '[microns]'

	import pylab
	
	n = 100
	x = []
	y = []
	xMin = 8
	xMax = 14
	increment = (xMax - xMin)/float(n)
	for i in range(n):
		x.append(xMin + i*increment)
	y = bb.spectral_radiance(x)
	
	pylab.figure()
	pylab.title('f(x) = sqrt(x)')
	pylab.xlabel('Wavelength [microns]')
	pylab.ylabel('Radiance [W / m^2 / micron / sr]')
	pylab.xlim([8,14])
	pylab.ylim([0,10])
	pylab.plot(x, y)
	pylab.show()
