import RPi.GPIO
import time

class UltrasonicDistanceSensor(object):
	"""
	UltrasonicDistanceSensor class
        class members
	
		triggerPin [Broadcom GPIO pin specification]
		echoPin [Broadcom GPIO pin specification]
            
	Author: Lindsay Martinescu
	"""
	def __init__(self, trigger, echo):
		"""
        	Initialize the instance with the provided values
		Args:
			triggerPin [Broadcom GPIO pin specification]
			echoPin [Broadcom GPIO pin specification]
		Author:
			Lindsay Martinescu
        	"""
		self.triggerPin = trigger
		self.echoPin = echo
		RPi.GPIO.setmode(RPi.GPIO.BCM)
		
	def __str__(self):
		"""
		Compute a prettier version 
		Return:
			a more readable form of the information
		Author:	
			Lindsay Martinescu	
		"""
		return 'Trigger Pin = ' + str(self.triggerPin) + \
			 'Echo Pin = 8' + str(self.echoPin) + \
			 '[Broadcom GPIO Pin Specification]'
		
	def distance (self, speedOfSound = 343.59999999999997):
		"""
        	Measure the amount of time it takes to read GPIO.HIGH \
			 from the echo pin
		Return:
			the elasped time
		Author:
			Lindsay Martinescu
        	"""
		RPi.GPIO.setup(self.triggerPin, RPi.GPIO.OUT)
		RPi.GPIO.output(self.triggerPin, RPi.GPIO.LOW)
		RPi.GPIO.setup(self.echoPin, RPi.GPIO.IN)
		time.sleep(.5)
		tStart = None
		tStop = None
		RPi.GPIO.output(self.triggerPin, RPi.GPIO.HIGH)
		time.sleep(1e-5)
		RPi.GPIO.output(self.triggerPin, RPi.GPIO.LOW)
		while RPi.GPIO.input(self.echoPin) == RPi.GPIO.LOW:
			pass
		tStart = time.time()
		while RPi.GPIO.input(self.echoPin) == RPi.GPIO.HIGH:
			pass
		tStop = time.time() 
		if tStart == None or tStop == None:
			tElasped = 0
		else:
			tElasped = tStop- tStart 
		distance = (tElasped/ 2) * speedOfSound #meter / second
		return distance
	
	def cleanup (self):
		"""
		Cleanup after, basically, reset the GPIO  
		Author:
			Lindsay Martinescu
		"""
		RPi.GPIO.cleanup()

if __name__ == "__main__":

	import gpio

	# Ultrasonic distance sensor #1
	sensor1Trigger = 10
	sensor1Echo = 25
	# Ultrasonic distance sensor #2
	sensor2Trigger = 9
	sensor2Echo = 8
	# Ultrasonic distance sensor #3
	sensor3Trigger = 11
	sensor3Echo = 7

	sensor1 = gpio.UltrasonicDistanceSensor(sensor1Trigger, sensor1Echo)
#	sensor2 = gpio.UltrasonicDistanceSensor(sensor2Trigger, sensor2Echo)
#	sensor3 = gpio.UltrasonicDistanceSensor(sensor3Trigger, sensor3Echo)

	try:
		while True:
			print 'Sensor 1: %.3f' % sensor1.distance(), 'meters'
#			print 'Sensor 2: %.3f' % sensor2.distance(), 'meters'
#			print 'Sensor 3: %.3f' % sensor3.distance(), 'meters'
	except KeyboardInterrupt:
		sensor1.cleanup()
#		sensor2.cleanup()
#		sensor3.cleanup()
