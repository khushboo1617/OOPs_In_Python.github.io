class A:
	def show(self):
		print('hello')
		
class B(A):
	def show(self):
		print('bye')
		
a = A()
a.show()