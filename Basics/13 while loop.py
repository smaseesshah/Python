#Password Verification
new_password=int(input("Enter New Password : "))
password=int(input("Enter Password to Log in : "))
while password!=new_password:
    password=int(input("Enter Correct Password : "))
print("Log in Successful!")