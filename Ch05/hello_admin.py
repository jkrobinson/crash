# user_names = []
user_names = ['fred', 'mary', 'anahita', 'admin', 'azadeh', 'sarah']

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print(f"Hello {user_name}, would you like to see a status report?")
        else:
            print(f"Hello {user_name.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
