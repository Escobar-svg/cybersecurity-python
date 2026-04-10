# login.py

correct_username = "admin"
correct_password = "12345"

attempts = 3

print("=== Secure Login System ===")

while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Access Granted ✅")
        break
    else:
        attempts -= 1
        print("Access Denied ❌")
        print(f"Attempts left: {attempts}")

if attempts == 0:
    print("Account locked 🔒")