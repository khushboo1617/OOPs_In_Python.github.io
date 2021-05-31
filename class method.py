class student:
	school='parul university'
	
	@classmethod
	def info(cls):  #classmethod
		return cls.school
		
print(student.info())