

def login_page():
    username = "user"
    password = "admin"

    max_attempt = 3
    attempt = max_attempt

    while attempt > 0:
        uname = input("Enter Username: ")
        paswrd = input("Enter Password: ")

        if uname == username and paswrd == password:
            print("Login Success !!!")
            break
        elif uname == username and paswrd != password:
            attempt -= 1
            print(f"Wrong password, Try Again!!  Attempt Left: {attempt}")
        elif paswrd == password and uname != username:
            attempt -= 1
            print(f"Wrong Username, Try Again!!   Attempt Left: {attempt}")
        else:
            attempt -= 1
            print(f"Username and Password both wrong, Try Again !!!  Attempt Left: {attempt}")

    
    if attempt == 0:
        print("Maximum number of attempts reached. Please try again later.")

login_page()