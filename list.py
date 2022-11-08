#spam = ['cat','bat','rat','elephant']
# for data in spam:
#     print(data)
# 

# print(spam[1])
# print(spam[2])
# print(spam[3])
# print(spam[-1])
# print(spam[-2])
# print(spam[-3])
# print(spam[-4])
# spam =[['cat','bat'],[10,20,30,40,50]]
# print(spam[0])
#print(spam[1])
# print(spam[0][1])
# print(spam[1][4])

# spam =['cat','bat','rat','elephant']
# print(spam[-1])
#print(spam)
#print(spam[0:4])
# print(spam[1:4])
# print(spam[0:-1])
# print(spam[:2])
# print(spam[1:])
# print(spam[:])
# print(len(spam))
# spam[1] ='dolon'
# print(spam)
catNames=[]
while True:
    print('Enter the name of cat '+str(len(catNames) + 1) + '(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are:')
for name in catNames:
    print(''+name)
