
pa_ss = input("Password: ")
while True: 
    re_password = input("Repeat password: ")
    if(pa_ss != re_password):
        print("They do not match!")
    else: 
        print("User account created!")
        break