#From car(car.py) file accesing Car(Car Class) and ElectricCar(ElectricCar Class)
from car import Car,ElectricCar

my_corola_obj = Car('voxwogan','Bere',2019)
print(my_corola_obj.get_description_name())

my_tesla_obj = ElectricCar('tesla','roadster',2019)
print(my_tesla_obj.get_description_name())