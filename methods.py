class student:
	college='parul' #class variable
	
	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2
		
def avg(self) : #Instance method
    return (self.m1 + self.m2)/2
    
def get_m1(self):  #accessor method
    return self.m1
    	
def set_m1(self,value):#mutator method
    self.m1=value
    	
s1=student(20,45)
s2=student(30,40)
		
		
#print(s1.avg())
print(s1.get_m1())


		