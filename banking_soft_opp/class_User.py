#parent class
class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name :" ,self.name)
        print("Age :" ,self.age)
        print("Gender :" ,self.gender)



#child Class
class Bank(User):
    def __init__(self,name,age,gender):
        super.__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = amount + self.balance
        self.balance = "Account Balance has update : $"+self.balance
        return self.balance


User_obj = Bank('dolon',42,'male',10)
print(User_obj.deposit(10))
#print(User_obj.show_details())


