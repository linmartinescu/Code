import RPi.GPIO
import time

class RCCircuit(object):
	"""
	RCCircuit class
        class members
		resistance (in ohms)
		capacitance (in farads)
		gpioPin
            
	Author: Lindsay Martinescu
	"""
	def __init__(self, resistance, capacitance, gpioPin):
		"""
        	Initialize the instance with the provided values
		Args:
			resistance [ohms]
			capacitance [farads]
			gpioPin
		Author:
			Lindsay Martinescu
        	"""
		self.resistance = resistance
		self.capacitance = capacitance
		self.gpioPin = gpioPin
		self.timeConstant = self.resistance * self.capacitance
		RPi.GPIO.setmode(RPi.GPIO.BCM)
        
	def __str__(self):
		"""
		Compute a prettier version 
		Return:
			a more readable form of the information
		Author:	
			Lindsay Martinescu
		"""

		return 'R = ' + str(self.resistance) + ' ohm(s), C = ' + \
			str(self.capacitance) + ' farad(s), t = ' + \
			str(self.timeConstant) + ' seconds'
    
	def discharge_capacitor(self, dischargeTime = 0):
		"""
		Discharge the capacitor by setting the selected GPIO pin to LOW
		Args:
			dischargeTime [seconds]
		Author:
			Lindsay Martinescu
		"""

	        RPi.GPIO.setup(self.gpioPin, RPi.GPIO.OUT) 
        	RPi.GPIO.output(self.gpioPin, RPi.GPIO.LOW) 
        	if dischargeTime == 0:  
			time.sleep( self.timeConstant * 10) 
        	else:
			time.sleep(dischargeTime)
    
    	def time_to_charge(self):
        	"""
        	Measure the amount of time it takes to read GPIO.HIGH \
			 from the selected pin
		Return:
			the time consant
		Author:
			Lindsay Martinescu
        	"""
		RPi.GPIO.setup(self.gpioPin, RPi.GPIO.IN)
        	start = time.clock()
       		while RPi.GPIO.input(self.gpioPin) == RPi.GPIO.LOW:
        		pass
		end = time.clock()
        	return  end - start
        
    	def cleanup (self):
        	"""
       		Cleanup after, basically, reset the GPIO  
		Author:
			Lindsay Martinescu
        	"""
        	RPi.GPIO.cleanup()
    
    
if __name__ == '__main__':
	resistance = 2200 #ohms
	capacitance = 0.000047 # farads
	gpioPin = 4
    
	rc = RCCircuit(resistance, capacitance, gpioPin)
	print rc
    
    	try:

        	while True:
            		rc.discharge_capacitor()
            		print '%.3f' % rc.time_to_charge(), ' seconds'
    	except KeyboardInterrupt:
        	rc.cleanup()
