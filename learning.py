class Dog():
	"""docstring for Dog"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + 'is now sitting')

	def roll_over(self):
		print(self.name.title() + "is rolling over")
		

my_dog = Dog('jame', 3)

my_dog.sit()
my_dog.roll_over()