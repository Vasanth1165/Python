class person:
	def __init__(self):
		self.name=input()
		self.gender=input()
		self.age=int(input())
	def talk(self):
		print("Hi, i am ",self.name)
	def gender(self):
		print(self.gender)
	def vote(self):
		if self.age >=18:
			print("You are eligible to vote")
		else:
			print("You are not eligible to vote")
obj=person()
person.talk(obj)
person.gender(obj)
person.vote(obj)
