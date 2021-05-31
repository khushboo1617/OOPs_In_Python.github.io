class A:
	def __init__(self): #constructor of A
		print('cinstructor of A')
		
class B(A):
	def __init__(self):
		super().__init__()#super keyword
		print('constructor of B')
		
		
'''a1= A()
b1= B()'''

b2=B()