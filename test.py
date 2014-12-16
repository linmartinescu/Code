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
