
# print(len("Hello")   )       # works on a string
# print(len(["a", "b", "c"]))  # works on a list
# print(len({"a": 1, "b": 2})) # works on a dictionary
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")        # Create a Car object
# boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
# plane1 = Plane("Boeing", "747")      # Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()

# # Output:
# # Drive!
# # Sail!
# # Fly!



class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")        # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")      # Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
