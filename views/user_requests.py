import sqlite3
import json
from datetime import datetime
from models import User


def login_user(user):
    """Checks for the user in the database

    Args:
        user (dict): Contains the username and password of the user trying to login

    Returns:
        json string: If the user was found will return valid boolean of True and the user's id as the token
                     If the user was not found will return valid boolean False
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select id, username
            from Users
            where username = ?
            and password = ?
        """, (user['username'], user['password']))

        user_from_db = db_cursor.fetchone()

        if user_from_db is not None:
            response = {
                'valid': True,
                'token': user_from_db['id']
            }
        else:
            response = {
                'valid': False
            }

        return json.dumps(response)


def create_user(user):
    """Adds a user to the database when they register

    Args:
        user (dictionary): The dictionary passed to the register post request

    Returns:
        json string: Contains the token of the newly created user
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Users (first_name, last_name, username, email, password, bio, created_on, active) values (?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            user['first_name'],
            user['last_name'],
            user['username'],
            user['email'],
            user['password'],
            user['bio'],
            datetime.now()
        ))

        id = db_cursor.lastrowid

        return json.dumps({
            'token': id,
            'valid': True
        })


def get_all_users():
    """Gets all users from the database

    Returns:
        json string: Contains a list of all users in the database
    """
    with sqlite3.connect('./db.sqlite3') as conn:

        # magic that allows us to access the columns by name instead of index
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL query to get all users
        db_cursor.execute("""
        SELECT 
            u.id, 
            u.first_name, 
            u.last_name, u.email, 
            u.bio, 
            u.username, 
            u.password, 
            u.profile_image_url, 
            u.created_on, 
            u.active
        FROM Users u
        """)

        # Create an empty list to hold all users
        users = []
        # Fetch all rows from the executed query and store them in the dataset variable
        dataset = db_cursor.fetchall()

        # Loop through the dataset and create User objects
        for row in dataset:
            user = User(
                row['id'],
                row['first_name'],
                row['last_name'],
                row['email'],
                row['bio'],
                row['username'],
                row['password'],
                row['profile_image_url'],
                row['created_on'],
                row['active']
            )
            # Append the user object to the list
            users.append(user.__dict__)

    return users


def update_user(user):
    """Updates a user in the database
    Args:
        user (dict): The dictionary passed to the update user post request
    Returns:
        json string: Contains the token of the updated user
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Update Users 
        Set first_name = ?, last_name = ?, username = ?, email = ?, password = ?, bio = ?, profile_image_url = ?
        Where id = ?
        """, (
            user['first_name'],
            user['last_name'],
            user['username'],
            user['email'],
            user['password'],
            user['bio'],
            user['profile_image_url'],
            user['id']
        ))

        return json.dumps({
            'token': user['id'],
            'valid': True
        })


def delete_user(user_id):
    """Deletes a user from the database

    Args:
        user_id (int): The id of the user to delete

    Returns:
        json string: Contains the token of the deleted user
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Delete from Users 
        Where id = ?
        """, (user_id,))

        return json.dumps({
            'token': user_id,
            'valid': True
        })


def get_user_by_id(user_id):
    pass
