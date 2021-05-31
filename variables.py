class House:
	main_door= 2 #class variable
	
	def __init__(self):
		self.doors= 10 #instance variable
		self.window_type= 'circle' #instance variable
		
room1=House()
room2= House()
	
print(room1.doors  , room1.window_type  , room1.main_door)
print(room2.doors  , room2.window_type  , room2.main_door)
	
House.main_door=1
print(room1.main_door)
print(room2.main_door)