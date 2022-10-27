#def greet_user():
#	print('Hello')

#greet_user()	

#def greet_user(username):
#	print(f"Hello {username}")

#greet_user('dolon')

#def describe_pet(animal_type,pet_name):
#	print(f"\nI have a {animal_type}")
#	print(f"{animal_type}'s name is {pet_name.title()}")

#describe_pet('hamset','herry')	

#def describe_pet(animal_type,pet_name):
#	print(f"\nI have a {animal_type}")
#	print(f"My {animal_type}'s name is {pet_name.title()}")

#describe_pet(animal_type='hamster',pet_name='harry')
#describe_pet(pet_name='harry',animal_type='hamster')
#def describe_pet(pet_name,animal_type='dog'):
#	print(f"\nI have a {animal_type}")
#	print(f"My {animal_type}'s name is {pet_name.title()}")

#describe_pet(pet_name='while')
#def get_formatted_name(first_name,last_name):
#	full_name = f"{first_name} {last_name}"
#	return full_name.title()

#musician = get_formatted_name('jimi','hendrix')

#print(musician)

#def get_formatted_name(first_name,middle_name, last_name=''):
#	full_name = f"{first_name} {middle_name} {last_name}"
#	return full_name.title()

#musician = get_formatted_name('john','lee','hooker')
#print(musician)	

#musician = get_formatted_name('jimi','hendrix')
#print(musician)

#def build_person(first_name,last_name):
#	person = {'first':first_name,'last':last_name}
#	return person

#musician = build_person('jimi','hedrix')
#print(musician)

#def get_formatted_name(first_name,last_name):
#	full_name = f"{first_name} {last_name}"
#	return full_name.title()

#while True:
#	print("\nPlease tell me your name")	
#	f_name = input("First Name:")
#	l_name = input("Last Name:")

#	formated_name = get_formatted_name(f_name,l_name)
#	print(f"\nHello, {formated_name}")

#def greet_users(names):
#	for name in names:
#		msg = f"Hello, {name.title()}"
#		print(msg)

#usernames = ['hunnah','ty','margot']
#greet_users(usernames)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models =[]
 
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Principal model: {current_design}")
	completed_models.append(current_design)
#Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)