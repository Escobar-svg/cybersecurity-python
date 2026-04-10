# login.py

import getpass
import time
from datetime import datetime

# correct credentials
correct_username = "admin"
correct_password = "12345"

# wordlists
usernames = ["admin", "root", "user", "test"]
passwords = ["1234", "password", "admin", "12345", "root"]

attempts = 3
lockout_time = 5

print("=" * 40)
print("      SECURE LOGIN SYSTEM")
print("=" * 40)


def log_attempt(username, password, status):
    with open("login_logs.txt", "a") as f:
        f.write(f"{datetime.now()} | {username} | {password} | {status}\n")


while attempts > 0:
    print("\n1. Manual Login")
    print("2. Brute Force Attack (demo)")
    choice = input("Choose option: ")

    # ---------------- manual login ----------------
    if choice == "1":
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if username == correct_username and password == correct_password:
            print("Access Granted ✅")
            log_attempt(username, password, "SUCCESS")
            break
        else:
            print("Access Denied ❌")
            log_attempt(username, password, "FAILED")
            attempts -= 1
            print("Attempts left:", attempts)

    # ---------------- brute force ----------------
    elif choice == "2":
        print("\nStarting brute force...\n")

        for user in usernames:
            for pwd in passwords:
                print(f"Trying {user}:{pwd}")

                if user == correct_username and pwd == correct_password:
                    print("\nCredentials Found!")
                    print(f"Username: {user}")
                    print(f"Password: {pwd}")
                    log_attempt(user, pwd, "BRUTE SUCCESS")
                    exit()

                log_attempt(user, pwd, "BRUTE FAILED")
                time.sleep(0.3)

    else:
        print("Invalid option")

# lockout
if attempts == 0:
    print("\nToo many failed attempts!")
    print(f"Locked for {lockout_time} seconds...")
    time.sleep(lockout_time)
    print("Try again later.")