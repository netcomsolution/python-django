class Employee:
#Constructor: A simple kind of method we use to initialize instance members
#It is used for initializing the instance members when we create the object of class
#Every class must have a constructor.Constructors can be two types:
# 1. Non Parameterized(Default) 2.Parameterized  
    # need constructor for initializing the value which is coming 
    # class
    def __init__(self,name,age,experience,salary):
        self.name = name
        self.age = age
        self.experience = experience
        self.salary = salary

    def describe(self):
        print('Here is Mr ',self.name,'.He is ',self.age,'year old and his salary',self.salary)







