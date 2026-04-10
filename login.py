# login.py

correct_username = "admin"
correct_password = "12345"

attempts = 3

while attempts > 0:
    print("\n=== LOGIN SYSTEM ===")
    
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print("Access Denied")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account Locked")