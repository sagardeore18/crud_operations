import mysql.connector

def get_mysql_connector():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="crud_operations")
    return mysqldb

def get_mysql_cursor(mysqldb):
    mysql_cursor=mysqldb.cursor()
    return mysql_cursor


def insert_into_mysql(roll_no, name, marks):
    mysqldb = get_mysql_connector()
    mysql_cursor = get_mysql_cursor(mysqldb)
    try:
        insert_query = f"insert into student_record(roll_no, name, marks) values({roll_no}, '{name}', {marks})"
        print(f"new query : {insert_query}")
        mysql_cursor.execute(insert_query)
        mysqldb.commit()
        print("Record inserted into the table")
    except:
        print("Error occurred")
        mysqldb.rollback()
    mysqldb.close()

#display record
def display_record(roll_no):   
    mysqldb = get_mysql_connector()
    mysql_cursor = get_mysql_cursor(mysqldb) 
    try:
        display_query = f"select * from student_record where roll_no= {roll_no}"
        print(f"new_query :{display_query}")
        mysql_cursor.execute(display_query)
        result= mysql_cursor.fetchall()
        for i in result:
            roll_no= i[0]
            name= i[1]
            marks= i[2]
            print(f"roll_no : {roll_no} , name : {name} , marks : {marks}")
    except:
        print("some issue in the code")
        mysqldb.rollback()
    mysql_cursor.close()   
    mysqldb.close()  

# TO update the record
def update_record(name, roll_no):
    mysqldb = get_mysql_connector()
    mysql_cursor = get_mysql_cursor(mysqldb)
    try:
        update_query= f"update student_record set name = '{name}' where roll_no = {roll_no}"
        print(f"new query : {update_query}")
        mysql_cursor.execute(update_query)
        mysqldb.commit()
        print("Record updated")
    except: 
        print("Error occurred")
        mysqldb.rollback()
    mysql_cursor.close()  
    mysqldb.close()

#  To delete the record
def delete_record(roll_no):
    mysqldb = get_mysql_connector()
    mysql_cursor = get_mysql_cursor(mysqldb)
    try:
        delete_query=f"delete from student_record where roll_no = {roll_no}"
        print(f"new query :{delete_query}")
        mysql_cursor.execute(delete_query)
        mysqldb.commit()
        print("Record delete")
    except:
        mysqldb.rollback()
    mysql_cursor.close()
    mysqldb.close()



