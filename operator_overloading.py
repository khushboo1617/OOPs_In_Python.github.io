class student:
	def __init__(self,m1,m2):
		self.m1= m1
		self.m2= m2

	def __add__(self,other):#operator overloading
		a1= self.m1 + other.m2
		a2= self.m1 + other.m2
		a3 = (a1 , a2)
		return a3
		
	def __gt__(self,other): #operator overloading
		r1 = self.m1 + self.m2
		r2 = other.m1+ other.m2
		if r1>r2:
			return True
		else:
			return False
		
		
s1 = student(26,50)
s2 = student(30,50)

print(s1 + s2)

if s1>s2:
	print('s1')
else:
		print('s2')