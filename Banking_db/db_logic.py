from use_db import use_database

connection = use_database()
cursor = connection.cursor()

def create_db_table():
    """function that create database """
    sql_query1 = "CREATE TABLE customer (cust_id int not null auto_increment primary key, first_name varchar(20), last_name varchar(30), middle_name varchar(30), dob varchar(20), mobile varchar(20), occupation varchar(20))"
    sql_query2 = "CREATE TABLE account (acc_num int not null primary key, cust_id_fk int, foreign key(cust_id_fk) references customer(cust_id), acc_type varchar(20), acc_status varchar(20), acc_dob varchar(20))"
    sql_query3 = "CREATE TABLE tansaction (trans_id int not null auto_increment primary key, acc_num_fk int, foreign key(acc_num_fk) references account(acc_num), trans_dob varchar(20), trans_type varchar(20), trans_amount int, trans_medium varchar(20))"

    cursor.execute(sql_query1)
    cursor.execute(sql_query2)
    cursor.execute(sql_query3)

    # check if table is created
    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    # print all table in database
    for table in tables:
        print(table)


# Collect input from user
def create_customer():
    """Fuction that add user to the database"""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    middle_name = input("Enter your middle name: ")
    dob = input("Enter your date of birth (YY-MM-DD): ")
    mobile  = input("Enter your mobile number: ")
    occupation = input("Enter your occupation: ")

    query = "INSERT INTO customer (first_name, last_name, middle_name, dob, mobile, occupation) values (%s,%s,%s,%s,%s,%s)"

    values = (first_name, last_name, middle_name, dob, mobile, occupation)

    cursor.execute(query, values)

    connection.commit()

    print(cursor.rowcount, "record added!")

def print_all_user():
    """Function that print out all the user in the database"""

    sql_query = "select * from customer order by first_name"

    cursor.execute(sql_query)

    records = cursor.fetchall()

    print("Total number of rows in customer is: ", cursor.rowcount)
    if records == 0:
        print("\n No customer in database!")
    else:
        print("\nPrinting each customer record")
        for record in records:
            print("Id = ", record[0], )
            print("First name = ", record[1])
            print("Last name  = ", record[2])
            print("Middle name = ", record[3])
            print("Date of birth  = ", record[4])
            print("Mobile number = ", record[5])
            print("Occupation  = ", record[6], "\n")


def delete_customer():
    """Function that delete user in the database"""
    id = int(input("Enter your id: "))

    query = "DELETE FROM customer WHERE cust_id = %s"

    cursor.execute(query, (id,))

    connection.commit()

    print(cursor.rowcount, "record(s) deleted!")


def update_customer():
    """Function that update user in the database"""
    print_all_user()

    id = int(input("Enter your id: "))
    new_value = input("Enter your new value: ")
   

    query= "UPDATE customer set first_name = %s where cust_id = %s"
    cursor.execute(query, (new_value, id))

    connection.commit()
