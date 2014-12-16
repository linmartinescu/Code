import math

class Vector(object):
	"""
	Class Vector
        class members
		x [default value must be 0]
		y [default value must be 0]
            
	Author: Lindsay Martinescu
	"""
	def __init__(self, x = 0.0, y = 0.0): 
		self.x = x
		self.y = y
	
		#This method must instantiate the object.

	def get_x(self):
		return self.x
		#This method must retrieve the current value of the vector's x-component from the object.

	def set_x(self,val):
		self.x = val
		#This method must change the current value of the vector's x-component in the object.

	def get_y(self):
		return self.y
		#This method must retrieve the current value of the vector's y-component from the object.

	def set_y(self,val):
		self.y = val
		#This method must change the current value of the vector's y-component in the object.

	def magnitude(self):
		#This method must return the magnitude (or geometric length) of the vector.
		return math.sqrt((self.x*self.x)+(self.y*self.y))
	
	def normalize(self):
		#This method must return the normalized form of the vector (the unit vector representation).
		# -- get magnitude of vector, then divide each component by that value
		return  Vector(self.x/self.magnitude(),self.y/self.magnitude())

	def __str__(self):
		return self.__repr__()
	
	def __repr__(self):
		return "<%s,%s>" % (self.x, self.y)
	
	def __len__(self):
		# the length of a vector is defined to be it's magnitude
		return self.magnitude()
	
	def __div__(self, other):
		# divide me by a scalar(number)
		return Vector(self.x/other,self.y/other)
		
	def __sub__(self, other):
		# subtract a scalar (number) from me
		return Vector(x-other,y-other)
	
	def __radd__(self, other):
		# add 2 vectors, when we are on right right side
		return Vector(self.x+other.x,self.y+other.y)

	def __add__(self, other):
		# add 2 vectors
		return Vector(self.x+other.x,self.y+other.y)

	def __abs__(self):
		# absolute value of a vector, which is defined as it's length or magnitude
		return self.magnitude()
	
	def __mul__(self,other):
		# multiply a vector * number
		return Vector(self.x*other,self.y*other)

	def __rmul__(self, other):
		# multiply a number * vector
		return Vector(self.x*other,self.y*other)
	
	def __eq__(self,other):
		return (self.x == other.x) & (self.y == other.y)
	
	

if __name__ == '__main__':

	import geometry
        
	v1 = geometry.Vector(4, 3)
	print 'v1 =', v1
	print 'Type of v1 =', type(v1)
	print 'x-component of v1 =', v1.get_x()
	print 'y-component of v1 =', v1.get_y()
	print 'Magnitude of v1 =', v1.magnitude()
	print 'Normalized v1 =', v1.normalize()

	v2 = geometry.Vector()
	print 'v2 =', v2
	v2.set_x(3)
	v2.set_y(4)
	print 'v2 =', v2
	print 'Type of v2 =', type(v2)
	print 'x-component of v2 =', v2.get_x()
	print 'y-component of v2 =', v2.get_y()
	print 'Magnitude of v2 =', v2.magnitude()
        print 'Length of v2 =', len(v2)
        print '|v1| = ', abs(v1)
	print 'Normalized v2 =', v2.normalize()

        v3 = geometry.Vector(3.0,4.0)
        print 'v3 = ', v3
	print 'v1 == v2 =', v1 == v2
	print 'v1 == v1 =', v1 == v1
	print 'v1 == v3 = ', v1 == v3
        print 'v2 == v3 = ', v2 == v3
        
        #test addition
	print 'v1 + v2 =', v1 + v2
	
        # test '__mul__'
	print 'v1 * 7 =', v1 * 7
	print '7 * v1 =', 7 * v1
        
        # test division
        print 'v3 / 2.0 = ', v3 / 2.0
        
	listVectors = [v1, v2, v3]
	print 'List of vectors [v1, v2, v3] =', listVectors
	
	tupleVectors = (v1, v2, v3)
	print 'Tuple of vectors (v1, v2, v3) =', tupleVectors