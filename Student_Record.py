if __name__ == "__main__":
    Student = []

    def show_menu():
        print("Select 1 for add\nSelect 2 for delete\nSelect 3 for upgrade\nSelect 4 for show\nSelect 5 for exit")
    print("Welcome to Student Record")
    show_menu()
    choice = int(input("Please select the action you want to perform : "))

    while choice !=5:
        
        
        
        match choice:
            case 1:
                Student.append(input("Please enter your student name: "))
            case 2:
                Student_Delete = input("please enter your student name for delete : ")
                if Student_Delete in Student:
                    Student.remove(Student_Delete)
                    print("delete is successful")
                else:
                    print("There is no Student who has a name that",Student_Delete)
                
            case 3:
                Student_Update = input("please enter your student name for upgrade : ")
                if Student_Update in Student:
                    index = Student.index(Student_Update)
                    New_Student_Name = input("Please enter new name : ")
                    Student[index] = New_Student_Name
                else:
                    print("There is no Student who has a name that",Student_Update)
                
            case 4:
                print(Student)
        
        show_menu()  
        choice = int(input("Please select the another action you want to perform : "))
        if choice == 5:
            print("Exiting... Have a nice Day")
            break

