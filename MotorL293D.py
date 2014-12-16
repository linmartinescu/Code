import RPi.GPIO
import time
import 
class MotorL293D(object):
	"""
	MotorL293D class
        class members
	
		motorControlPin [Broadcom GPIO pin specification]
		input1Pin [Broadcom GPIO pin specification]
		input2Pin [Broadcom GPIO pin specification]
            
	Author: Lindsay Martinescu
	"""

	def __init__(): 
		"""
		Initialize the instance with defult values 
		Args:
			input1Pin [Broadcom GPIO pin specification]
			input2Pin [Broadcom GPIO pin specification]
		Author:
			Lindsay Martinescu
        	"""
		self.input1Pin = input1
		self.input2Pin = input2
		self.motorControlPin = mortorControlPin
		self.pwm = pwm # 50 hz and duty cyle 0???
		self.direction = direction
		self.speed = speed
		direction = 0
		speed = 0
		RPi.GPIO.setmode(RPi.GPIO.BCM)
		RPi.GPIO.setup(self.input1Pin, RPi.GPIO.OUT)
		RPi.GPIO.output(self.input1Pin, RPi.GPIO.LOW)
		RPi.GPIO.setup(self.input2Pin, RPi.GPIO.OUT)
		RPi.GPIO.output(self.input2Pin, RPi.GPIO.LOW)
		RPi.GPIO.setup(self.motorControlPin, RPi.GPIO.OUT)
		#It must setup the provided L293D input pins ("input1Pin" and "input2Pin") as outputs and make sure that their state is LOW, setup the motor /
		#control pin ("motorControlPin") as an output, and setup a "pwm" object member with a frequency of 50 Hz and a duty cycle of 0./
		#It must also create a "direction" and "speed" member both with initial values of 0.
	def __set_direction():
		#This method must set the motor "direction" member to one of the following values
		#0 (0b00) - set both input pins LOW (free for some motors)
		#1 (0b01) - set input pin 1 LOW and input pin 2 HIGH
		#2 (0b10) - set input pin 1 HIGH and input pin 2 LOW
		#3 (0b11) - set both input pins HIGH (brake for some motors)
		#and change the motor's direction to match the provided state.

	def __get_directiion(): 
		#This method must get the motor's current direction

	def set_speed(): 
		#This method must set the motor "speed" member to a value in the range 0 to 100. This will represent the percentage of the
		#motor's maximum speed. This method should also be responsible for changing the motor's speed to match the provided value.
		#A positive or negative "speed" value must result in the appropriate change in motor direction.

	def get_speed(): 
		#This method must get the motor's current speed

	def brake():
		#This method must set the motor's "speed" to 0 an the "direction" to a brake setting if available.

	def stop():
		#This method must brake the motor and turn of the PWM control for that motor. This method should be used as a cleanup method.
		m.stop()
		
	def cleanup (self):
		"""
		Cleanup after, basically, reset the GPIO  
		Author:
			Lindsay Martinescu
		"""
		RPi.GPIO.cleanup()

if __name__ == '__main__':

	import gpio

	motorControlPin = 22
	input1Pin = 21
	input2Pin = 17
	motor = gpio.MotorL293D(motorControlPin, input1Pin, input2Pin)

	print "Turning motor clockwise at 100% speed"
	motor.set_speed(100)
	time.sleep(2)

	print "Braking the motor"
	motor.brake()
	time.sleep(2)

	print "Turning motor clockwise at 50% speed"
	motor.set_speed(50)
	time.sleep(2)

	print "Braking the motor"
	motor.brake()
	time.sleep(2)

	print "Turning motor counterclockwise at 50% speed"
	motor.set_speed(-50)
	time.sleep(2)

	print "Braking the motor"
	motor.brake()
	time.sleep(2)

	print "Turning motor counterclockwise at 100% speed"
	motor.set_speed(-100)
	time.sleep(2)

	print "Braking the motor"
	motor.brake()
	time.sleep(2)
	
	print "Stopping (cleaning up) the motor"
	motor.stop()
	time.sleep(2)

	RPi.GPIO.cleanup()

