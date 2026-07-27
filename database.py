import sqlite3
from user import User


def create_table():
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor() 

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_name TEXT UNIQUE,
        password TEXT,
        name TEXT,
        age INTEGER,
        stream TEXT,
        projectdescription TEXT,
        agenda TEXT,
        skills TEXT,
        current_stage TEXT
                     )
                         """)
    connect.commit()
    connect.close()

def add_user(user):
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()

    cursor.execute("""
        INSERT INTO  users (user_name, password,name, age, stream, projectdescription, agenda, skills, current_stage)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
          user.user_name ,
          user.password,
          user.name, 
          user.age, 
          user.stream, 
          user.projectdescription, 
          user.agenda, 
          user.skills,
          user.current_stage))

    connect.commit()
    connect.close()



def get_all_users():
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    user_objects = [ ]


    for row in rows:
        user = User(
                 row[0],
                 row[1],
                 row[2],
                 row[3],
                 row[4],
                 row[5],
                 row[6],
                 row[7],
                 row[8],
    )

        user_objects.append(user)



    connect.close()
    return user_objects 


def login(user_name, password):
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE user_name = ? AND password = ?",
        (user_name, password)
    )

    row = cursor.fetchone()

    connect.close()

    if row:
        return User(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8]
    )

    return None


import sqlite3

def update_user(user):

    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()

    cursor.execute("""
                UPDATE users
                SET
                name = ?,
                age = ?,
                stream = ?,
                projectdescription =  ? ,       
                agenda = ?,
                skills = ?,
                current_stage = ?,
            
            WHERE user_name  = ?   
        """, (
            user.name,
            user.age,
            user.stream,
            user.projectdescription,
            user.agenda,
            user.skills,
            user.current_stage,
            user.user_name

        ))

    connect.commit()
    connect.close()