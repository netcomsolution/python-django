# def teacher(name,designation,salray):
#     return(name,designation,salray)

# belal = teacher('balaa','teacher',3000)
# print(teacher('balaa','teacher',3000))
# print(belal)

# def shopkeeper(*args):
#     total = 0
#     for total_price in args:
#         total += total_price

#     return total


    
# print(shopkeeper(10,10,10,10,10,10,100,10,10,10))

purchaseitems = {'cahl':10,'dal':20,'oil':14}

def shop(**kwargs):
    total = 0
    value_data=[]
    for key,value in kwargs.items():
        total = total + value_data[value]
    return total

#print(purchaseitems)  
print(shop(purchaseitems))     
