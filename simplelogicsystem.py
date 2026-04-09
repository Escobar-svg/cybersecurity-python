# adding number of attempts
password = "admin123"
for i in range(3):
    user_input = input("Enter password: ")
    if user_input == password:
     print("ACCESS GRANTED")
     break
    else:
     print("WRONG PASSWORD")
else:
    print("ACCOUNT BLOCKED")
