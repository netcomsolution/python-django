def shop(*args):
    total = 0    
    for total_price in args:    
        total += total_price 
    return total

print(shop(20,202,20,289))