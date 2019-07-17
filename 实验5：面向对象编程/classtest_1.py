#!/usr/bin/env python3

class UserData:
	
	def __init__(self,id,name):
		self.id=id
		self.name=name
	
	def __repr__(self):
		return "ID:{} Name:{}".format(self.id,self.name)

class NewUser(UserData):
	
	group = 'shiyanlou-louplus'

	def get_name(self):
		return self.name
	
	def set_name(self,value):
		self.name=value
	
	def __repr__(self):
		return "ID:{} Name:{}".format(self.id,self.name)
	
	@classmethod
	def get_group(self):
		return self.group 

	@staticmethod
	def format_userdata(id,name):
		return "{}'s id is {}".format(name,id)

if __name__ == "__main__":
	#user1 = UserData(101,'Jack')
	#user2 = UserData(102,'Louplus')
	#print(user1)
	#print(user2)

	#user1 = NewUser(101,'Jack')
	#user1.set_name('Jackie')
	#user2 = NewUser(102,'Louplus')
	#print(user1)
	#print(user2)

	print(NewUser.get_group())
	print(NewUser.format_userdata(100,'Lucy'))
