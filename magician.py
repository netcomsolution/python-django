#magicians = ['alice','david','carolina']
#for magician in magicians:
#print(magicians[:2])
	#print(f"{magician.title()}, that was a great trick!")
#print(f"I can wait for next trick,{magician.title()}.\n")
#print("thank you")
#my_foods = ['pizza','falafel','carrot cake']
#friend_foods = my_foods[:]

#print("My favorite foods are:")
#print(my_foods)
#print("\nMy friends favorite foods are:")
#print(friend_foods)

#my_foods = ['pizza','falafel','carrot cake']
#friend_foods = my_foods[:]

#my_foods.append("cannoli")
#friend_foods.append("ice cream")
#print("My favorite foods are:")
#print(my_foods)

#print("\nMy friends favourite foods are:")
#print(friend_foods)

#cars = ['audi','bmw','subaru','toyota']
#for car in cars:
#	if car == 'bmw':
#		print(car.upper())
#	else:
#		print(car.title())
#age = 12
#if age > 4:
	#print("Your admission cost is $0")
#	price = 0
#elif age > 18:
	#print("Your admission cost is $25")
#	price = 25
#else:
	#print("Your admission cost is $40")
#	price = 40
#print(f"Your admission cost is :{price}")
#alien_0 = {'color':'green'}
#print(alien_0['color'])	
#alien_0 = {'color' : 'green','points':5}
#new_points = alien_0['points']
#print(f"you just earned {new_points}")
#alien_0 = {'color':'green','points':5}
#print(alien_0)

#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)
#alien_0 ={}
#alien_0['color'] = 'green'
#alien_0['points'] = 5
#print(alien_0)
#alien_0 = {'color':'green'}
#print(f"The alien is {alien_0['color']}")

#alien_0['color'] = 'Yellow'
#print(f"The alien is {alien_0['color']}")

#alien_0 = {'x_position':0, 'y_position':25, 'speed': 'medium'}
#print(f"Orginal position:{alien_0['x_position']}")

#alien_0['speed'] = 'fast'
#if alien_0['speed'] =='slow':
#	x_increment = 1
#elif alien_0['speed'] == 'medium':
#	x_increment = 2
#elif alien_0['speed'] == 'fast':
#    x_increment = 3

#alien_0['x_position'] = alien_0['x_position']+x_increment


#print(f"New position:{alien_0['x_position']}")  

#favorite_languages = {
#	'jen' : 'python',
#	'sarah' : 'c',
#	'edward' : 'ruby',
#	'phil' : 'python',
#}  

#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is:{language}")
#alien_0 = {'color':'green','speed':'slow'}
#point_value = alien_0.get('points','No point value assigned')
#print(point_value)
#favorite_languages = {
#	'jen':'python',
#	'sarah' : 'c',
#	'edward' : 'ruby',
#	'phil' : 'python',
#}

#for name,language in favorite_languages.items():
#	print(f"{name.title()}'s favorite language is {language.title()}")

#for name in sorted(favorite_languages.keys()):
#	print(f"here is {name.title()}")
#if 'wein' not in favorite_languages.keys():
#	print("Erin,please take your poll!")
#for language in set(favorite_languages.values()):

#	print(f"Here is language {language.title()}")
#alien_0 = {'color':'green','points':5}
#alien_1 = {'color':'yellow','points':10}
#alien_2 = {'color':'red','points':15}

#aliens = [alien_0,alien_1,alien_2]

#for alien in aliens:
#	 print(alien)
#aliens =[]
#for alien_number in range(30):
#	new_alien = {'color':'green','points':'5','speed':'slow'}
#	aliens.append(new_alien)

#for alien in aliens[:5]:
#	print(alien)	

#print(f"Total Number of aliens:{len(aliens)}")
#aliens =[]
#for alien_number in range(30):
#	new_alien = {'color':'green','points':5,'speed':'slow'}
#	aliens.append(new_alien)


#for alien in aliens[:3]:
#	if alien['color'] == 'green':
#		alien['color'] = 'yellow'
#		alien['speed'] = 'medium'
#		alien['points'] = 10

#for alien in aliens[:5]:
#	print(alien)

#pizza ={'crust':'thik','toppings':['mushrooms','extra chegese']}

#print(f"You orderes a {pizza['crust']}-crust pizza with the following toppings:")	

#for topping in pizza['toppings']:
#	print("\t" + topping)	

#favorite_languages = {
#	'jen':['python','ruby'],
#	'sarah' : ['c'],
#	'edward' : ['ruby','go'],
#	'phil' : ['python','haskell'],
#	}


#for name,languages in favorite_languages.items():
#	print(f"\n{name.title()}'s favorite languages are:")
#	for language in languages:
#			print(f"\t{language.title()}")	
#users ={
#	'aeinstein':{
#					'first' : 'albert',
#					'last' : 'einstein',
#					'location' : 'princeton',
#				},
#	'mcurie': {
#			
#			'first' : 'marie',
#			'last'  : 'curie',
#			'location' : 'paris',
#	},			
#}

#for username, user_info in users.items():
#	print(f"\nUsername:{username}")
#	full_name = f"{user_info['first']} {user_info['last']}"
#	location = user_info['location']

#	print(f"\tFull Name:{full_name.title()}")
#	print(f"\tLocaton:{location.title()}")
#message = input("Tell me something, and i will repeat it back to you: ")
#print(message)
#age = input("How old are you?")
#age >= 18
#height = input("How tall are you,in inches?")
#height = int(height)

#if height >=48:
#	print("\nYou are tall enough to ride!")
#else:
#	print("\nYou will be able to ride when you are a litter older")
#number = input("Enter a number, and i will tell you if it's even or odd:")
#number = int(number)

#if number%2==0:
#	print(f"\nThe number {number} is even")
#else:
#	print(f"The number {number} is odd")
#current_number =1
#while current_number <=5:
#	print(current_number)
#	current_number +=1
responses = {}
polling_active = True

while polling_active:
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to climb someday?")

	responses[name] = response

	repeat = input("Would you like to let another person respond ? (yes/no)")
	if repeat == 'no':
		polling_active = False

print("\n---Polling Result---")
for name,response in responses.items():
	print(f"{name} would like to climb {response}")	
