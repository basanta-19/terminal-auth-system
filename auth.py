# TERMINAL-BASED USER AUTHENTICATION SYSTEM WITH SECURE PASSWORD HASHING AND SESSION MANAGEMENT

import bcrypt

from users import users_db
current_user = None

def register_user(username, password):
    if username in users_db:
        return "Username already exists."
    
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    
    users_db[username] = hashed
    return("Registration Successful!!")
    
def login(username, password):
    global current_user
    if current_user is not None:
            return(f"The user {current_user} is already logged in. Please log out this account.")
    if username not in users_db:
            return("Invalid Username!!")
    
    elif bcrypt.checkpw(password.encode(), users_db[username]): 
        current_user = username
        return("Logged in Successfully!!")
      
    else:
        return("Incorrect Password")

def logout():
    global current_user
    
    if current_user is None:
        return("No user is logged in.")
    
    else:
        user = current_user
        current_user = None
        return(f"The account {user} Logged out successfully!!")
        
while True:
    choice = int(input("Enter 1 for registration, 2 for login and 3 for exit and 4 for log out: "))
    if(choice == 1):
        username = input("Username: ")
        password = input("Password: ")
        print(register_user(username, password))
    
    elif(choice == 2):
        username = input("Username: ")
        password = input("Password: ")
        print(login(username, password))
        
    elif choice == 3:
        break
    
    elif choice == 4:
        print(logout())