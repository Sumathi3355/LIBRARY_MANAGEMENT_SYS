print("Library Management System Login")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login successful")
        print("Welcome to Library System")
    else:
        print("wrong password")
else:
    print("Invalid user")

print("Program ended")
