import crud 

def main():
    # roll_no = input("enter roll number : ")
    # name =  input("enter name : ")
    # marks =  input("enter marks : ")
    # crud.insert_into_mysql(roll_no=roll_no, name=name, marks=marks)
    # crud.update_record(name=name, roll_no=roll_no)
    # crud.display_record(roll_no=roll_no)
    # crud.delete_record(roll_no=roll_no)
    while(True):
        print("1.Insert_record")

        print("2.Update_record")

        print("3.Delete_record")

        print("4.Display_record")
         
        print("5.Exit")

        print()

        selection = int(input("Enter your choice : "))
        print(f"selection: {selection} ")
    
        if (selection == 1):
            roll_no = input("Enter roll_no : ")
            name = input("Enter name : ")
            marks = input("Enter marks : ")
            crud.insert_into_mysql(roll_no, name, marks)
        elif (selection == 2):
            roll_no = input("Enter roll_no : ")
            name = input("Enter name")
            crud.update_record(roll_no=roll_no, name=name)
        elif (selection == 3):
            roll_no = input("Enter roll_no : ")
            crud.delete_record(roll_no=roll_no)
        elif (selection == 4):
            roll_no = input("Enter roll_no : ")     
            crud.display_record(roll_no=roll_no)
        elif (selection == 5):
            break
        else:
            print("Wrong choice ")
        

if __name__ == '__main__':
    main()