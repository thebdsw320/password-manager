# Authentication system 
from database import create_connection, create_user
from encryption import create_keys

def signup_user(username: str):
    """
    Create a new user

    Parameters:
        username: str -> Username 
    
    Returns:
        user_id: int -> User ID
    """
    connection = create_connection('./db/sqlite.db')
    
    
    user = (username,)
    user_id  = create_user(connection, user)
    
    key_files = create_keys(username)