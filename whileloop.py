#Exercise 01
# current_number = 0
# while current_number <=10:
#     #print(current_number)
#     current_number +=1
#     if current_number % 2 ==0:
#         print(current_number)
'''
Exercise 01 result
2
4
6
8
10
'''
#Exercise 02 Write a while loop that adds all the numbers up to 100
# counter=0
# total=0
# while total <=100:
#     #total += 1
#     print(total)

prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end program\n"

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print("Please Write quit to end program")    