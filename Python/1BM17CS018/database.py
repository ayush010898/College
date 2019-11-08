import sqlite3

def create(conn):
    conn.execute('''CREATE TABLE EMPLOYEE
                (ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                AGE INT NOT NULL,
                SALARY REAL);''')
    print("Table successfully created in the database.")

def insert(conn):
    conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,SALARY) VALUES (1, 'AAKASHDEEP', 21, 20000.00 )")
    conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,SALARY) VALUES (2, 'ADITYA', 25, 15000.00 )")
    conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,SALARY) VALUES (3, 'ADHYAYAN', 23, 20000.00 )")
    conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,SALARY) VALUES (4, 'ANJALI', 22, 65000.00 )")
    conn.commit()
    print("Records created successfully")

def update(conn):
    conn.execute("UPDATE EMPLOYEE set SALARY = 25000.00 where ID = 1")
    conn.commit()

def delete(conn, id):
    conn.execute("DELETE from EMPLOYEE where id = " + str(id) + ";")
    conn.commit()

def display(conn):
    cursor = conn.execute("SELECT id, name, salary from EMPLOYEE")
    print('Data in the database table: ')
    print()
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("SALARY = ", row[2])
    print()

conn = sqlite3.connect('pythonsqlite.db')
choice = 0
while choice != 6:
    print('EMPLOYEE DATABASE')
    print('1. CREATE')
    print('2. INSERT')
    print('3. UPDATE')
    print('4. DELETE')
    print('5. DISPLAY')
    print('6. QUIT')

    choice = int(input('Enter the choice: '))
    if choice == 1:
        create(conn)
    elif choice == 2:
        insert(conn)
    elif choice == 3:
        update(conn)
    elif choice == 4:
        id = int(input('Enter the employee id to be deleted: '))
        delete(conn,id)
    elif choice == 5:
        display(conn)
    elif choice == 6:
        break
