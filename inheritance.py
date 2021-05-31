class A:
	def feature1(self):
		print('hii! , from A1')
	
	def feature2(self):
		print('hii! , from A2')
		
	
class B(A):#single inheritence
	def feature3(self):
		print('hii! , from B1')
	def feature4(self):
		print('hii! , from B2')
	
	
class C(B):#multilevel inheritence
	def feature5(self):
		print('hii! , from C1')
	
	
#class D(A,C):#multiple inheritence
	def feature6(self):
		print('hii! , from D1')
		
a1= A()
b1= B()
c1= C()
#d1= D()

a1.feature1()
b1.feature2()
c1.feature5()
'''d1.feature5()
d1.feature2()
d1.feature6()'''
c1.feature2()