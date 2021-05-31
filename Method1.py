class student:
	
	def __init__(self,m1,m2):
		self.m1=m1
		self.m2=m2
		
	
	def average(self):
		return (self.m1 + self.m2 )/2
		
		
s1=student(50,60)
s2=student(50,80)
		
t=s1.average()
print(t)