#From othe file accessing to file(car.py) and  importing  class(Car)
from car import Car
my_new_car_obj = Car('audi','a4',2009)
#Accessing method of other class(Car Class) via object/intance(my_new_car_obj)
print(my_new_car_obj.get_description_name())
#Accesing to variable via object/intance
my_new_car_obj.odometer = 23
#Accessing method of other class(Car Class) via object/intance(my_new_car_obj)
my_new_car_obj.read_odometer()