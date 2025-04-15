#Did this project with guidance from W J Pearce on YouTube
import hashlib
import getpass

password_manager = {}

#To create an account with a sha256 algorithm
def create_account():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully! ")

#To log in with that created account
def logIn():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful! ")
    else:
        print("Invalid username or password. ")

#Creating the small menu option
def main():
    while True:
        choice = input("Enter 1 to create and account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            logIn()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

#A way to tell the code which function goes first   
if __name__ == "__main__":
    main()