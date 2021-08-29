student_list = []

def add_student():
	roll = int(input("Enter the roll number (integer) of student : "))
	name = input("Enter the name (string) of student : ")
	phone = list(input("Enter the multiple contact numbers (comma seprated) of student : ").split(','))
	branch = input("Enter the branch (string) of student : ")
	location = input("Enter the location (string) of student : ")
	city = input("Enter the city (string) of student : ")
	pincode = input("Enter the pincode (string) of student : ")
	phy = float(input("Enter the marks of physics (float) of student : "))
	che = float(input("Enter the marks of chemistry (float) of student : "))
	mat = float(input("Enter the marks of maths (float) of student : "))
	hin = float(input("Enter the marks of hindi (float) of student : "))
	eng = float(input("Enter the marks of english (float) of student : "))
	address = {'location':location, 'city':city, 'pincode':pincode}
	marks = {'phy':phy ,'che':che ,'mat':mat ,'hin':hin ,'eng':eng}
	data = {roll:[name,phone,branch,address,marks]}
	print("\n\nYou added roll no. ",roll, "successfully.\n\n")
	student_list.append(data) 
	print(student_list)

def delete_student():
	data = int(input("Enter the roll no. you want to delete."))
	for x in student_list:
		y = list(x.keys())
		if y[0] == data:
			student_list.remove(x)
	print(student_list)

def search_student():
	data = int(input("Enter the roll no. you want to search."))
	for x in student_list:
		y = list(x.keys())
		if y[0] == data:
			print(x)

def search_branch():
	data = input("Enter the branch of the students you want to search.")
	for x in student_list:
		y = list(x.values())
		if y[0][2] == data:
			print(x)

def search_subject():
	a,b = map(str, input("Enter subject and the minimum marks : ").split(' '))
	for x in student_list:
		y = list(x.values())
		if y[0][4][a] > float(b):
			print(x)

def search_topper():
	totals = list()
	for x in student_list:
		y = list(x.values())
		temp = 0
		print()
		for i in list(y[0][4].values()):
			temp = temp + i
		totals.append(temp)
	print("-----Topper Of The Class Is-------")
	print(student_list[totals.index(max(totals))])

def showMenu():
	print("\n#----------------OPTIONS---------------#")
	print("#------------SELECT ANY NUMBER-------------#\n")
	print("1. Add Student")
	print("2. Delete Student")
	print("3. Search Student")
	print("4. Search Student By Branch")
	print("5. Search Student By Subject")
	print("6. Search Topper")
	print("7. Exit\n")
	
	opt = int(input("Enter Your Option : "))

	if opt<1 or opt>7:
		print("\n !!!!!!!!! Please Choose Correct Option !!!!!!!!\n")
		showMenu()
	elif opt==1:
		print("\nYou Choosed : ",opt,"\n")
		add_student()
		showMenu()
	elif opt==2:
		print("\nYou Choosed : ",opt,"\n")
		delete_student()
		showMenu()
	elif opt==3:
		print("\nYou Choosed : ",opt,"\n")
		search_student()
		showMenu()
	elif opt==4:
		print("\nYou Choosed : ",opt,"\n")
		search_branch()
		showMenu()
	elif opt==5:					
		print("\nYou Choosed : ",opt,"\n")
		search_subject()
		showMenu()
	elif opt==6:
		print("\nYou Choosed : ",opt,"\n")
		search_topper()
		showMenu()
	else:							
		print("\nYou Choosed : ",opt,"\n")
		print("\n\n#----------Thannk You---------- #\n\n")	

showMenu()




