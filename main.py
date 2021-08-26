import add_student as add
import delete_student as delete
import search_branch as branch
import search_student as student
import search_subject as subject
import search_topper as topper

def showMenu():
	print("\n#----------------OPTIONS---------------#")
	print("#------------SELECT ANY NUMBER-------------#\n")
	print("1. Add Student")
	print("2. Delete Student")
	print("5. Search Student")
	print("3. Search Student By Branch")
	print("4. Search Student By Subject")
	print("6. Search Topper")
	print("7. Exit\n")
	
	opt = int(input("Enter Your Option : "))

	if opt<1 or opt>7:
		print("\n !!!!!!!!! Please Choose Correct Option !!!!!!!!\n")
		showMenu()
	elif opt==1:
		print("\nYou Choosed : ",opt,"\n")
		add.add()
	elif opt==2:
		print("\nYou Choosed : ",opt,"\n")
		delete.delete()
	elif opt==3:
		print("\nYou Choosed : ",opt,"\n")
		student.search()
	elif opt==4:
		print("\nYou Choosed : ",opt,"\n")
		branch.search()
	elif opt==5:					
		print("\nYou Choosed : ",opt,"\n")
		subject.search()
	elif opt==6:
		print("\nYou Choosed : ",opt,"\n")
		topper.search()
	else:							
		print("\nYou Choosed : ",opt,"\n")
		print("\n\n#----------Thannk You---------- #\n\n")	

showMenu()





# [{rol1:student1} ,{student2}]


# roll : int
# name : str
# phone : set
# branch : str
# address : dict (location,city,pincode)
# marks : dict (phy,che,math,hin,eng)



# 1. Add Student
# 2. Search Student
# 3. Delete Student
# 4. Branch Filter
# 5. Subject Filter (Greater Than)
# Sub : che
# number : 45
# 6. Topper
# 7. Exit