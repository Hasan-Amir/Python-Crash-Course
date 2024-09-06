"""3-6. More Guests: You just found a bigger dinner table, so now more
space is available. Think of three more guests to invite to dinner.
Start with your program from Exercise 3-4 or 3-5. Add a print() call to
the end of your program, informing people that you found a bigger table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list."""
guests = ["Ali", "Ibrar", "Nadeem", "Ibtisam"]
print(f"Dear {guests} we found a bigger tabble")
guests.insert(0, "Asghar")
guests.insert(2, "Nosheen")
guests.append("Radhika")
print(f"Dear {guests[0]}, Welcome to dinner")
print(f"Dear {guests[1]}, Welcome to dinner")
print(f"Dear {guests[2]}, Welcome to dinner")
print(f"Dear {guests[3]}, Welcome to dinner")
print(f"Dear {guests[4]}, Welcome to dinner")
print(f"Dear {guests[5]}, Welcome to dinner")
print(f"Dear {guests[6]}, Welcome to dinner")
