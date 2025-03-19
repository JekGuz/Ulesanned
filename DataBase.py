#C:\Users\kotik\source\repos\Ulesanned\AppData

from sqlite3 import *
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = connect(path)
        print("Ühendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis viga '{e}'")
    return connection

#МБ открытие можно в самый конец
conn=create_connection("C:/Users/kotik/source/repos/Ulesanned/AppData/data.db")

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Table on loodud või andmed on sisestatud")
    except Error as e:
        print(f"Viga '{e}' tabli loomisega")

create_user_table = """
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
nationality TEXT
);
"""

execute_query(conn, create_user_table)

# ОБЯЗАТЕЛЬНО СНАЧАЛА ГЕНДЕР, чтобы было с чего подставлять
# Делаем новую таблицу
create_gender_table= """
CREATE TABLE IF NOT EXISTS gender(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
nimetus TEXT NOT NULL)
"""
execute_query(conn, create_gender_table)

create_gender="""
INSERT INTO
gender(nimetus)
VALUES
('🐀'),
('🐍')"""

execute_query(conn, create_gender)



# Новая таблица, для того чтобы сделать ее с фторичным ключем и соединить таблицы
create_user_table2 = """
CREATE TABLE IF NOT EXISTS users2(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
lname TEXT NOT NULL,
age INTEGER,
gender INTEGER,
FOREIGN KEY (genderID) REFERENCES gender (Id)
);
"""
execute_query(conn, create_user_table2)

create_users2 = """
INSERT INTO
users2 (name, lname, aeg, genderID)
VALUES
('Mati', 'Tamm', 25, 1)
('Kate', 'Koom', 35, 2)
('Margus', 'Lol', 22, 1)
('Anna', 'Kusk', 33, 2)
"""
execute_query(conn, create_users2)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Viga '{e}' ")

# create_users = """
# INSERT INTO
#  users (name, age, gender, nationality)
# VALUES
#  ('Mati', 25, 'mees', 'USA'),
#  ('Linda', 32, 'naine', 'England'),
#  ('Brigitte', 35, 'naine', 'England'),
#  ('Mike', 40, 'mees', 'Denmark'),
#  ('Elizabeth', 21, 'naine', '🐍');
#  """

# execute_query(conn, create_users)

select_users="SELECT * from users"
users = execute_read_query(conn, select_users)
for user in users:
    print(user)

# обращаемся сразу к двум таблицам
select_users2="SELECT * from users2"
select_users_gender = """
SELECT
users2.name
users2.lname
gender.nimetus
from users2
INNER JOIN gender ON users2.genderID = gender.ID"""

select_users2="SELECT * from users2"
users2 = execute_read_query(conn, select_users2)
for user in users2:
    print(user)


# # Variant 1
# def add_users_query(connection, user_data):
#     query = "INSERT INTO users(name, age, gender, nationality) VALUES(" + user_data + ")"
#     execute_query(connection, query)

# insert_user = "('" + input("Nimi: ") + "','" + input("Vanus: ") + "','" + input("Sugu: ") + "','" + input("Riik: ") + "')"
# print(insert_user)

# add_users_query(conn, insert_user)


# # Variant 2
# def add_users_query_2(connection, user_data):
#     """Lisame userit, mis on eraldi sisestatud"""
#     query = "INSERT INTO users(name, age, gender, nationality) VALUES(?, ?, ?, ?)"
#     cursor = connection.cursor()
#     cursor.execute(query, user_data)
#     connection.commit()

# insert_user = (input("Nimi: "), int(input("Vanus: ")), input("Sugu: "), input("Riik: "))

# print(insert_user) 
# add_users_query_2(conn, insert_user)

# def delete_data_from_tabel(connection, query):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(query)
#         connection.commit()
#         print("Andmed on kustutatud")
#     except Error as e:
#         print(f"Viga '{e}' andmete kustutamisega")

# print("Andmete kustutame tabelist 'users'")
# delete_data_from_users = "DELETE FROM users WHERE age < 30"
# delete_data_from_tabel(conn, delete_data_from_users)
# print("Tabelis 'users' on jäänud neid kes vanem kui 30:")
# users = execute_read_query(conn, select_users)

for user in users:
    print(user)


