#!/usr/bin/env python3

class UserData():
	def __init__(self,id,name):
		self.id=id
		self._name=name

class NewUser(UserData):
	
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self,value):
		try:
			if len(value)<=3:
				raise ValueError()
			else:
				self._name = value
		except ValueError:
			print("ERROR")

	def __call__(self,*args,**kwargs):
		print("{}'s id is {}".format(self.name,self.id))
		

if __name__ == "__main__":
	#user1=NewUser(101,'Jack')
	#user1.name='Lou'
	#user1.name = 'Jackie'
	#user2=NewUser(102,'Louplus')
	#print(user1.name)
	#print(user2.name)
	
	user = NewUser(101,'Jack')
	user()
