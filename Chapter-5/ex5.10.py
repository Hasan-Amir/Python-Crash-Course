"""5-10. Checking Usernames: Do the following to create a program that
simulates how websites ensure that everyone has a unique username.
Make a list of five or more usernames called current_users.
Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)"""
users: list[str] = ["Ahmad", "Ali", "Noor", "Admin","Subhan", "Mubashir"]
nusers: list[str] = ["Kabir", "Soha", "ali", "Mubashir"]
usersl = [user.lower() for user in users]
# for user in users:
#     usersl.append(user.lower())
nusersl = [user.lower() for user in nusers]
# for user in nusers:
#     nusersl.append(user.lower())

for user in nusersl:
    if user in usersl:
        print(f"{user}: username already exits, choose a different user name.")
    else: print(f"{user}: username is available.")
