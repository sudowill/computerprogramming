newpassword = input("BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber', '123', 'password123']
newpassword = input("Pick a new password (8-12 characters): ")
passwordset = input("Please enter the new password: ")
if newpassword in BAD_PASSWORDS:
    print("You're predicable, choose another one")
else:
    if len(newpassword) >= 8 and len(newpassword) <= 12 and newpassword == passwordset:
        print("Password Set")
    else:
        print("The two passwords are not the same and they must be a length between 8 and 12 characters")
