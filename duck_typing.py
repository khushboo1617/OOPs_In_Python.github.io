class visual_studio:
	def execute(self):
		print('compile it')
		print('run it')

class sublime:
	def execute(self):
		print('grammar check')
		print('run')
		
class student:
	def coding(self,ide):
		ide.execute()
		

stu1 = student()
#ide = visual_studio()
ide = sublime()
stu1.coding(ide)