import mysql.connector

def insert_into_mysql(roll_no, name, marks):
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="crud_operations")
    mysqlcursor=mysqldb.cursor()
    #mysqlcursor.execute("create table student_record(roll_no INT, name VARCHAR(30), marks INT)")
    inser_student_query = f"insert into student_record(roll_no, name, marks) values({roll_no}, '{name}', {marks})"
    try:
        mysqlcursor.execute(inser_student_query)
        mysqldb.commit()
        print("Record inserted into the table")
    except:
        print("Error occured..")
        mysqldb.rollback()
    mysqldb.close()

def main():
    roll_no = input("enter roll number : ")
    name =  input("enter name : ")
    marks =  input("enter marks : ")
    insert_into_mysql(roll_no=roll_no, name=name,marks=marks)


if __name__ == '__main__':
    main()