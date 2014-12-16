#!/usr/bin/env python
if __name__ == '__main__':
	    
#	from radiometry import bb_temperature
        import radiometry
        
	wavelength = 10 # microns
	trueTemperature = 300 # Kelvin
	
	bb = radiometry.Blackbody(wavelength, trueTemperature)
	radiance = bb.radiance()
	
	temperature = radiometry.bb_temperature(wavelength, radiance, epsilon=1e-6)
	print 'T =', temperature, '[K]'
	print 'for a blackbody emitting', radiance, '[W / m^2 / micron / sr]'
	print 'at', wavelength, '[microns]'
	
	temperature = radiometry.bb_temperature(wavelength, radiance, epsilon=1e-2)
	print 'T =', temperature, '[K]'
	print 'for a blackbody emitting', radiance, '[W / m^2 / micron / sr]'
	print 'at', wavelength, '[microns]'
	
	temperature = radiometry.bb_temperature(wavelength, radiance)
	print 'T =', temperature, '[K]'
	print 'for a blackbody emitting', radiance, '[W / m^2 / micron / sr]'
	print 'at', wavelength, '[microns]'
	
	
	
	
	