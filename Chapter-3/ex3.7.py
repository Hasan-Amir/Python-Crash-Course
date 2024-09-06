"""3-7. Shrinking Guest List: You just found out that your new dinner table
won’t arrive in time for the dinner, and now you have space for only two
guests.
Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
Print a message to each of the two people still on your list, letting them
know they’re still invited."""
guests = ['Asghar', 'Ali', 'Nosheen', 'Ibrar', 'Nadeem', 'Ibtisam', 'Radhika']
print(f"We are sorry {guests}, we can only invite two people for dinner")
poped_guest = guests.pop()
print(f"We are sorry {poped_guest}, we can not invite you for dinner")
poped_guest = guests.pop()
print(f"We are sorry {poped_guest}, we can not invite you for dinner")
poped_guest = guests.pop()
print(f"We are sorry {poped_guest}, we can not invite you for dinner")
poped_guest = guests.pop()
print(f"We are sorry {poped_guest}, we can not invite you for dinner")
poped_guest = guests.pop()
print(f"We are sorry {poped_guest}, we can not invite you for dinner")
print(f"Our final guests are: {guests}")
print(f"Dear {guests[0]}, you are still invited for dinner")
print(f"Dear {guests[1]}, you are still invited for dinner")
del guests[0]
del guests[0]
print(guests)