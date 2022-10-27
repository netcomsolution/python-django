#exercise 01
# lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
# for data in lst:
#     print(data)

'''
Exercise 01 Result:
koala
cat
fox
panda
chipmunk
sloth
penguin
dolphin
'''    

#Exercise 02 
# lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
# for data in lst:
#     print('Hello '+data)

'''
Exercise 02 Result:
Hello Sam
Hello Lisa
Hello Micha
Hello Dave
Hello Wyatt
Hello Emma
Hello Sage
'''
#Exercise 03 Write a for loop that iterates through a string and prints every letter.


# str="Antarctica"
# for data in str:
#     print(data)
'''
Exercise 03 result
A
n
t
a
r
c
t
i
c
a
'''

#Exercise 04 Using a for loop and .append() method append each item with a Dr. prefix to the lst.
# lst1=["Phil", "Oz", "Seuss", "Dre"]
# lst2=[]
# for data in lst1:
#     lst2.append("Dr. "+data)

# print(lst2)

'''
Exercise 04 result
['Dr. Phil', 'Dr. Oz', 'Dr. Seuss', 'Dr. Dre']
'''

#Exercise 05 Write a for loop which appends the square of each number to the new list.

# lst1=[3, 7, 6, 8, 9, 11, 15, 25]
# lst2=[]
# for data in lst1:
#     lst2.append(data **2)
# print(lst2)
'''
Exercise 05 result
[9, 49, 36, 64, 81, 121, 225, 625]
'''
# Exercise 06 Write a for loop using an if statement, that appends each number to  positive data to positive 
# negitive will be in negative 
# raw_data =[111, 32, -9, -45, -17, 9, 85, -10]
# positive_data=[]
# negative_data=[]
# for data in raw_data:
#     if data > 0:
#         positive_data.append(data)
#     else:
#         negative_data.append(data)

# print(positive_data)
# print(negative_data)
'''
Exercise 06 result
[111, 32, 9, 85]
[-9, -45, -17, -10]
'''
# Exercise 06 
# raw_data=[3.14, 66, "Teddy Bear", True, [], {}]
# int_data=[]
# string_data=[]
# float_data=[]
# booler_data=[]
# bool_data=[]
# special_data=[]

# for data in raw_data:
#     if type(data) == int:
#         int_data.append(data)
#     elif type(data) == float:
#         float_data.append(data)
#     elif type(data) == str:
#         string_data.append(data)
#     elif type(data) == bool:
#         bool_data.append(data)
#     else:
#         special_data.append(data)


# print(int_data)
# print(float_data)   
# print(string_data) 
# print(bool_data)    
# print(special_data)

'''
Exercise 06 result

[66]
[3.14]
['Teddy Bear']
[True]
[[], {}]
'''

#Exercise 07 key value store 
dictonary_data = {'a': 3, 'b': 1, 'c': 2}
key_data=[]
value_data=[]
for key,value in dictonary_data.items():
    key_data.append(key)
    value_data.append(value)


print(key_data)
print(value_data)

'''
['a', 'b', 'c']
[3, 1, 2]
'''