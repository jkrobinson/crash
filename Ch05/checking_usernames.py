current_users = ['fred', 'mary', 'anahita', 'azadeh', 'sarah']
new_users = ['harry', 'henry', 'Anahita', 'alice', 'sarah']

current_checking = current_users[:]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Username {new_user.title()} in use.  Please try another name.")
    else:
        print(f"Username {new_user.title()} is available.")
