class Calculator:
    def addition(self,value1,value2):
        total = value1+value2
        return total

    def substraction(self,value1,value2):
        substract = value2-value1
        return substract

    def multiply(self,value1,value2):
        result = value1*value2
        return result

    def division(self,value1,value2):
        result = value2/value1
        return result
    
calculator_obj= Calculator()
print(calculator_obj.addition(10,20))   
print(calculator_obj.substraction(10,20)) 
print(calculator_obj.multiply(10,20)) 
print(calculator_obj.division(10,20)) 