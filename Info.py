class Info:
	pass
	def __init__(self,name,father_name,age,address):
		self.name = name
		self.father_name = father_name
		self.age = age
		self.address = address

	def student_create_roll(self):
		roll = self.name + self.age
		return roll




#print(one_class.student_create_roll())

class Teacher(Info):
	pass
	def __init__(self,name,father_name,age,address,spouse_name):
		super().__init__(name,father_name,age,address)
		self.spouse_name = spouse_name

	def teacher_create_id(self):
		tid = self.name + self.age + self.spouse_name
		return tid
	#overriding method(student_create_roll) that locate in parent class
	def student_create_roll(self):
		roll = self.name + self.age + self.father_name
		return roll


one_class_student = Info("Adeena",'Sakhawat Hossain','9','South Pirerbag Amtola')
one_class_teacher = Teacher("Bristi",'Molla Hossain','28','Amtola','Rafiq')
#calling method(student_create_roll) from parent class(Info)
print(one_class_student.student_create_roll())
#calling method(teacher_create_id) from child class(Teacher) which inheriting all value from parent class except spuse name
print(one_class_teacher.teacher_create_id())
#Now calling overridding method from child class
print(one_class_teacher.student_create_roll())
#help(one_class_teacher)