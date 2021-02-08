from mysql.connector import Error


def select_data():
    import mysql.connector
    from mysql.connector import Error
    try:
        mydb=mysql.connector.connect(host="localhost",user="rekha",passwd="1234",database="family")

        my_cursor=mydb.cursor()
        # q="insert into employee(emp_name,emp_id,sex) values (%s,%s,%s)"
        # v=[("ritvik",3,"M"),("pranav",4,"M"),("kiran",5,"M")]
        # my_cursor.executemany(q,v)
        # result_set1=my_cursor.fetchall()
        # for i in result_set1:
        #      print(i)
        q1="select count(*) from employee"
        my_cursor.execute(q1)
        result_set=my_cursor.fetchall()
        print(result_set)
    except Error as e:
        print("Database operation failed")
        print(e)
    finally:
        mydb.commit()
        my_cursor.close()

def fetch_data():
    import mysql.connector as mc

    try:

        db = mc.connect(host="localhost", user="rekha", passwd="1234", database="family")

        my_cursor = db.cursor()

        q = "select * from student"

        my_cursor.execute(q)

        records = my_cursor.fetchall()

        for i in records:
            print("name:", i[0])
            print("id:", i[1])
            print("sex:", i[2])

    except Error as e:
        print("Error reading data from database")
    finally:
        db.commit()

        db.close()



def update_data():
    import mysql.connector as mc
    try:

        db=mc.connect(host="localhost",user="rekha",passwd="1234",database="family")
        my_cursor=db.cursor()
        q="update student set roll_no=410 where name='rekha'"
        my_cursor.execute(q)
    except Error as e:
        print("Error reading data from database")
        print(e)
    finally:
         db.commit()

         db.close()
def insert_data(name,roll_no,age,section):
    l1=(name,roll_no,age,section)
    import mysql.connector as mc
    try:
        mydb=mc.connect(host="localhost",user="rekha",passwd="1234",database="family")
        my_cursor=mydb.cursor()
        q="insert into student (name,roll_no,age,section) values (%s,%s,%s,%s)"
        my_cursor.execute(q,l1)
    except Error as e:
        print("data base insertion error")
        print(e)
    finally:
        mydb.commit()
        mydb.close()




def get_data():
    if(__name__=="__main__"):

        select_data()
        update_data()
        fetch_data()
        insert_data("baby", "411", "4", "CSIT")
get_data()