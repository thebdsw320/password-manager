# Store passwords with hashes
import rsa, os
from typing import Tuple

def create_keys(username: str) -> Tuple:
    """
    Create keys for a new user to store his passwords securely
    
    Parameters:
        username: str -> Username to create keys

    Returns:
        files: Tuple -> File paths of keys (private and public)
    """
    
    public_key, private_key = rsa.newkeys(1024)
    
    public_key_pkcs1pem = public_key.save_pkcs1().decode('utf8')
    private_key_pkcs1pem = private_key.save_pkcs1().decode('utf8')
    
    keys_folder = os.path.join(
        os.getcwd(),
        'keys'
    )
    
    if not os.path.exists(keys_folder):
        os.mkdir(keys_folder)
    
    with open(f'./keys/{username}-public.pem', 'w+') as public:
        public.write(public_key_pkcs1pem)
    
    with open(f'./keys/{username}-private.pem', 'w+') as private:
        private.write(private_key_pkcs1pem)
        
    files = (f'./keys/{username}-public.pem', f'./keys/{username}-private.pem')
    
    return files

def encrypt_password(password_to_encrypt: str, username: str) -> bytes:
    """
    Encrypt password with public key of specified user
    
    Parameters:
        password_to_encrypt: str -> Password to encrypt
        username: str -> Username of user that wants to encrypt a password
    
    Returns:
        encrypted_password: bytes -> Encrypted password
    """
    with open(f'./keys/{username}-public.pem', 'rb') as public:
        keydata = public.read()
    
    public_key = rsa.PublicKey.load_pkcs1(keydata)
    
    encoded_password = password_to_encrypt.encode('utf8')
    encrypted_password  = rsa.encrypt(encoded_password, public_key)
    
    return encrypted_password

def decrypt_password(password_to_decrypt: bytes, username: str) -> str:
    """
    Decrypt password with private key of specified user
    
    Parameters:
        password_to_decrypt: str -> Password to decrypt
        username: str -> Username of user that wants to decrypt a password
    
    Returns:
        decrypted_password: str -> Decrypted password
    """
    with open(f'./keys/{username}-private.pem', 'rb') as private:
        keydata = private.read()
    
    private_key = rsa.PrivateKey.load_pkcs1(keydata)
    
    decrypted_password = rsa.decrypt(password_to_decrypt, private_key).decode()
    
    return decrypted_password