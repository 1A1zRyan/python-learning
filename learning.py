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

class Battery():
	"""docstring for Battery"""
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		"""打印电瓶信息"""
		print("This car has a " + str(self.battery_size) + "-kWh battery")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge"
		print(message)

class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make, model, year):
		''' 初始化父类属性 '''
		super().__init__(make, model, year)
		self.battery = Battery()

	
		

my_tesla = ElectricCar('telsa', 'model_s', 2016)	
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


