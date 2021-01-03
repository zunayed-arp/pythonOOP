'''Exercise Question 1: Create a Vehicle class with max_speed and
mileage instance attributes'''
class Vehicles:
 def __init__(self, name, max_speed, mileage):
  self.name = name
  self.max_speed = max_speed
  self.mileage = mileage

model_X = Vehicles(200,20)
print(model_X.max_speed, model_X.mileage)

''' Exercise Question 3: Create child class Bus 
that will inherit all of the variables and methods of the Vehicle class
'''
class Bus:
 pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name)

