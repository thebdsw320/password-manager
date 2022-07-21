# Create a new SQLite DB and connect with it

import sqlite3, os
from sqlite3 import Error, Connection
from typing import Optional, Tuple
from encryption import encrypt_password

def create_connection(db_file: str) -> Optional[Connection]:
    """ 
    Create a database connection to the SQLite database specified by db_file
    
    Parameters:
        db_file: str -> Database file
    
    Returns:
        connection: Optional[Connection] -> Connection or None
    """
    connection = None
    
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return connection


def create_table(connection: Connection, create_table_sql: str) -> None:
    """ 
    Create a table from the create_table_sql statement
    
    Ṕarameters: 
        connection: Connection
        create_table_sql: str -> SQL statement

    Returns:
        None
    """
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main_db() -> None:
    """
    Creates users and passwords tables on db/ folder
    """
    sql_folder = os.path.join(
        os.getcwd(),
        'db'
    )

    if not os.path.exists(sql_folder):
        os.mkdir(sql_folder)

    database = os.path.join(sql_folder, 'sqlite.db')

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL );"""

    sql_create_passwords_table = """CREATE TABLE IF NOT EXISTS passwords (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    password text NOT NULL,
                                    user_id integer NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id) );"""

    connection = create_connection(database)

    # Create tables
    if connection is not None:
        # Create projects table
        create_table(connection, sql_create_users_table)
        # Create tasks table
        create_table(connection, sql_create_passwords_table)
    else:
        print("Error! cannot create the database connection.")

def create_user(connection: Connection, user: Tuple) -> Optional[int]:
    """
    Creates a user in users table of database
    
    Parameters:
        connection: Connection
        user: Tuple -> (username,)
        
    Returns:
        user_id: Optional[int] -> ID of created user
    """
    statement = """ INSERT INTO users(username)
                VALUES(?) """
                
    cursor = connection.cursor()
    cursor.execute(statement, user)
    
    connection.commit()
    
    user_id = cursor.lastrowid
    
    return user_id
    
        
def store_password(name:str, password: str, user_id: int, username: str) -> Optional[int]:
    """
    Creates a password in passwords table of database
    
    Parameters:
        name: str 
        password: str
        user_id: int
        username: str 
        
    Returns:
        password_id: Optional[int] -> ID of created password
    """
    connection = create_connection('./db/sqlite.db')
    
    statement = """ INSERT INTO passwords(name, password, user_id)
                VALUES(?,?,?) """

    password = encrypt_password(password, username)
    
    password_tuple = (name, password, user_id)
    
    cursor = connection.cursor()
    cursor.execute(statement, password_tuple)
    
    connection.commit()
    
    password_id = cursor.lastrowid
    
    return password_id

def get_user_id(username: str) -> Optional[int]:
    connection = create_connection('./db/sqlite.db')
    statement = """ SELECT id FROM users WHERE username=? """
    cursor = connection.cursor()

    try:
        cursor.execute(statement, (username,))
        data = cursor.fetchall()
        return data[0][0]
    
    except Exception:
        return None

def get_all_passwords(user_id: int) -> Optional[list]:
    connection = create_connection('./db/sqlite.db')
    statement = """ SELECT name, password FROM passwords WHERE user_id=? """
    cursor = connection.cursor()

    try:
        cursor.execute(statement, (user_id,))
        data = cursor.fetchall()
        return data
    
    except Exception:
        return None