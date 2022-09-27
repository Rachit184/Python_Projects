import string
import random

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "" .join(password)
    print(password)
    print("Thank You")

option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes" or option == "yes":
    generate_password()
elif option == "No" or option == "no":
    print("Thank You")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()