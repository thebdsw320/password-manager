# Password Manager CLI
# Basic Functionalities
# - Store Passwords ✅
# - Generate Random Passwords with custom inputs (ex. length, special chars) ✅
# - Search for a specific password with given website or app name ⭕️
# - Authentication system to store passwords of different users ✅
# - Cool terminal dashboard ⭕️
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import print

from authentication import signup_user
from database import main_db, get_user_id, store_password, get_all_passwords
from encryption import decrypt_password
from password import create_password

import os

print("""
                    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
                    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
                    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
                    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
                    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
                    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝     
                                                                            (by @bdswtech)                                                                                                                      
      """)

print(Panel(Text("Here you can signup to start storing securely your passwords", justify='center')))
print("[bold red]To exit the program, press Ctrl+C\n")

while True:
    try:
        instruction = Prompt.ask('What do you want to do?\n', choices=['Signup', 'See my stored passwords', 'Store a new password'], default='Signup')
        if instruction == 'Signup':
            username = Prompt.ask('Create a new username')
            sql_folder = os.path.join(
                os.getcwd(),
                'db'
            )

            if not os.path.exists(sql_folder):
                main_db()
            
            user_id = signup_user(str(username))
            
            print('[bold green] User created succesfully, now you can start storing passwords\n')
            
        elif instruction == 'Store a new password':
            username = Prompt.ask('\n👉 What is your username?')
            user_id = get_user_id(username)
            
            if not user_id:
                print('[bold red]That username does not exist in the database, please signup or check it again')
                continue
            
            print('\n[bold cyan]How do you want your password?')
            password_name = Prompt.ask('💬 Password name (ex. GitHub, DigitalOcean, AWS)')
            randomize = Confirm.ask('🤸 Do you want a completely random password?')
            if not randomize:
                alphabet_count = Prompt.ask('🅰️  How many alphabet characters do you want to include in your new password?')
                numbers_count = Prompt.ask('#️⃣  How many numeric characters do you want to include in your new password?')
                special_count = Prompt.ask('*️⃣  How many special characters do you want to include in your new password? [!@#$%^&*()]')
                
                password = create_password(
                    alphabet_count=int(alphabet_count),
                    numbers_count=int(numbers_count),
                    special_chars_count=int(special_count),
                    randomize=randomize   
                )
                
            else:
                password = create_password()
            
            password_id = store_password(
                name=password_name,
                password=password,
                user_id=user_id,
                username=username
            )

            print('\n🎉 [bold green] Password saved succesfully\n')
        
        elif instruction == 'See my stored passwords':
            username = Prompt.ask('\n👉 What is your username?')
            user_id = get_user_id(username)
            
            if not user_id:
                print('[bold red]That username does not exist in the database, please signup or check it again')
                continue
            
            data = get_all_passwords(user_id)
            
            table = Table(title=f"{username}'s passwords")
            
            table.add_column('Name', style='cyan')
            table.add_column('Password', justify='left', style='green')
            
            for password in data:
                name = password[0]
                rawpass = decrypt_password(password[1], username)
                
                table.add_row(name, rawpass)
                
            
            console = Console()
            print('\n')
            console.print(table)
            print('\n')
            
        else:
            print('\n[red bold]Please choose a correct option\n')
            
    except KeyboardInterrupt:
        print('[bold red]\n\nExiting the program')
        break
