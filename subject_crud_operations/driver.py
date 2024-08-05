import crud


def main():
    # subject_id = input("enter subject_id : ")
    # subject_name =  input("enter subject_name : ")
    # teacher_id =  input("enter teacher_id : ")
    # crud.insert_into_mysql(subject_id=subject_id, subject_name=subject_name, teacher_id=teacher_id)
    # crud.update_record(subject_name=subject_name, subject_id=subject_id)
    # crud.display_record(subject_id=subject_id)
    # crud.delete_record(subject_id=subject_id)
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
            subject_id = input("Enter subject_id : ")
            subject_name = input("Enter subject_name : ")
            teacher_id = input("Enter teacher_id : ")
            crud.insert_into_mysql(subject_id, subject_name, teacher_id)
        elif (selection == 2):
            subject_id = input("Enter subject_id : ")
            subject_name = input("Enter subject_name")
            crud.update_record(subject_id=subject_id, subject_name=subject_name)
        elif (selection == 3):
            subject_id = input("Enter subject_id : ")
            crud.delete_record(subject_id=subject_id)
        elif (selection == 4):
            subject_id = input("Enter subject_id : ")     
            crud.display_record(subject_id=subject_id)
        elif (selection == 5):
            break
        else:
            print("Wrong choice ")
        

if __name__ == '__main__':
    main()