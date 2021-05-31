class student:#outer class
	
	def __init__(self, name, id):
		self.name=name
		self.id= id
		self.add= self.address()
		
	def show(self):
			print(self.name, self.id , end=' ')
			self.add.show()
			
		
			
	class address: #inner class
		def __init__(self):
			self.state='gj'
			self.dis= 'dk'
			self.h_no= 234
#this show()method is diff from above because it's of inner class.			
		def show(self):
			print(self.state, self.dis , self.h_no)
			
				
s1=student ('khushu',123)
s2=student ('kooo', 346)
s1.show()

add1 = student.address()
add2 = student.address()
#always create inner class inside of outer class.