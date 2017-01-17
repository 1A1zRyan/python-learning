class Car():
	"""docstring for Dog"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model

	def read_odmeter(self):
		print("This car has"self.model.title() + 'is now sitting')

	def roll_over(self):
		print(self.model.title() + "is rolling over")
		

my_dog = Dog('jame', 3)

my_dog.sit()
my_dog.roll_over()