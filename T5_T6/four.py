users = [{"username": "avishkar", "password": "password"}]


def password_check(password1, passwword2):
    if password1 == passwword2:

        return True


def signin(username, password):
    user_names = [
        (user_name.get("username"), user_name.get("password")) for user_name in users
    ]
    if (username, password) in user_names:
        print("You are logged in")
    else:
        print("wrong username or password")


def main():
    counter = 0
    username = input("Enter the username ")
    while counter < 3:
        password = input("Enter the password ")
        password_confirmation = input("Enter the password again ")
        if password_check(password, password_confirmation):
            signin(username, password)
            break
        else:
            print("wrong password please try again!")
            counter += 1
            if counter == 3:
                print("You have run out of tries")


if __name__ == "__main__":
    main()
