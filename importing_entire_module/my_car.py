#Importing file(car.py)
import car

#accessing to Car Class via file(car.py)
my_corola_obj = car.Car('voxwogan','Bere',2019)
print(my_corola_obj.get_description_name())
#accessing to ElectricCar Class via file(car.py)
my_tesla_obj = car.ElectricCar('tesla','roadster',2019)
print(my_tesla_obj.get_description_name())