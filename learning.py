class Car():
	"""docstring for Dog"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odmeter(self):
		print("This car has" + str(self.odometer) + 'miles on it.')

	def update_odometer(self, mileage):
		if mileage > self.mileage:
			self.odometer = mileage
		else:
			print("You can't roll back on odometer.")
	def increment_odometer(self, miles):
		self.odometer += miles



	
		




