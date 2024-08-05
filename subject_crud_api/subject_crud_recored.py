import mysql.connector
def get_mysql_connector():
    mysqldb=mysql.connector.connect(host="localhost", user="root", password="root", database="crud_operations")
    return mysqldb
    #mysqlcursor=mysqldb.cursor()
    #mysqlcursor.execute("create table subjects(subject_id int(20), primary key, subject_name varchar(30), teacher_id int(20)")
    #mysqlcursor.execute("insert into subjects (subject_id, subject_name, teacher_id) values(1, English, Ram sir)")
    #mysqldb.commit()
    #print("Record inserted into the table")
    #mysqldb.close()

def get_mysql_cursor(mysqldb):
        mysql_cursor=mysqldb.cursor()
        return mysql_cursor

def insert_into_mysql(subject_id, subject_name, teacher_id):
        mysqldb = get_mysql_connector()
        mysql_cursor = get_mysql_cursor(mysqldb)
        try:
            insert_query = f"insert into subjects(subject_id,subject_name,teacher_id) values({subject_id}, '{subject_name}', {teacher_id})"
            print(f"new query : {insert_query}")
            mysql_cursor.execute(insert_query)
            mysqldb.commit()
            print("Record inserted into the table")
        except:
            print("Error occurred")
            mysqldb.rollback()
        mysqldb.close()



def display_record(subject_id):
    mysqldb = get_mysql_connector()
    mysql_cursor = get_mysql_cursor(mysqldb)
    result = []
    try:
        display_quuery = f"select * from subjects where subject_id = {subject_id}"
        print(f"new_query :{display_quuery}")
        mysql_cursor.execute(display_quuery)
        result = mysql.cursor.fetchall()
    except:
        print("some issue in the code")
        mysqldb.rollback()
    mysql_cursor.close()
    mysqldb.close()
    return result
    


def update_record(subject_name, subject_id):
    mysqldb = get_mysql_connector()
    mysql_cursor = get_mysql_cursor(mysqldb)
    try:
        update_query= f"update subjects set subject_name = '{subject_name}' where subject_id = {subject_id}"
        print(f"new query : {update_query}")
        mysql_cursor.execute(update_query)
        mysqldb.commit()
        print("Record updated")
    except: 
        print("Error occurred")
        mysqldb.rollback()
    mysql_cursor.close()  
    mysqldb.close()      

def update_teacher(subject_id, teacher_id):
    mysqldb = get_mysql_connector()
    mysql_cursor = get_mysql_cursor(mysqldb)
    try:
        update_query= f"update subjects set teacher_id = '{teacher_id}' where subject_id = {subject_id}"
        print(f"new query : {update_query}")
        mysql_cursor.execute(update_query)
        mysqldb.commit()
        print("Record updated")
    except: 
        print("Error occurred")
        mysqldb.rollback()
    mysql_cursor.close()  
    mysqldb.close()      



def delete_record(subject_id):
    mysqldb = get_mysql_connector()
    mysql_cursor = get_mysql_cursor(mysqldb)
    try:
        delete_query=f"delete from subjects where subject_id = {subject_id}"
        print(f"new query :{delete_query}")
        mysql_cursor.execute(delete_query)
        mysqldb.commit()
        print("Record delete")
    except:
        print("Error occurred")
        mysqldb.rollback()
    mysql_cursor.close()
    mysqldb.close()

