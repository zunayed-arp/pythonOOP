'''Exercise Question 1: Create a Vehicle class with max_speed and
mileage instance attributes'''
class Vehicles:
 def __init__(self, max_speed, mileage):
  self.max_speed = max_speed
  self.mileage = mileage

model_X = Vehicles(200,20)
print(model_X.max_speed, model_X.mileage)

