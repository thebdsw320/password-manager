# Random Password Generator

import string, random
from typing import Optional

alphabets: list = list(string.ascii_letters)
numbers: list = list(string.digits)
special_chars: list = list('!@#$%^&*()')

def create_password(
    alphabet_count: Optional[int] = 0, 
    numbers_count: Optional[int] = 0, 
    special_chars_count: Optional[int] = 0, 
    randomize: bool = True
    ) -> str:
    
    """
    Creates a password from given inputs, number of characters from alphabet, numbers and special characters including (!@#$%^&*())

    Parameters:
        alphabet_count: Optional[int] = 0 -> Number of alphabet characters
        numbers_count: Optional[int] = 0 -> Number of digits 
        special_chars_count: Optional[int] = 0 -> Number of special characters 
        randomize: bool = True -> If True, randomly pick all the above parameters
    
    Returns:
        password: str -> Randomly generated password
        
    Examples:
        >>> my_random_password = create_password(randomize=True)
        >>> print(my_random_password)
        >>> '4w&!0Elg)Qvqn#l59@8t'
        
        >>> my_random_password = create_password(alphabet_count=10, numbers_count=5, special_chars_count=3, randomize=False)
        >>> print(my_random_password)
        >>> 'ej4H9$&%mUqr2L9w0w' 
        >>> # It has the same amount of characters that were specified above
    """
    
    password: list = []
     
    if randomize:
        alphabet_count = random.randint(8, 12)
        numbers_count = random.randint(5, 8)
        special_chars_count = random.randint(3, 5)
    
    for i in range(alphabet_count):
        password.append(
            random.choice(alphabets)
        )
    
    for i in range(numbers_count):
        password.append(
            random.choice(numbers)
        )
        
    for i in range(special_chars_count):
        password.append(
            random.choice(special_chars)
        )
    
    random.shuffle(password)
    
    return ''.join(password)