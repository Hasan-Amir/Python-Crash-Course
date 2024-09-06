"""3-5. Changing Guest List: You just heard that one of your guests can’t
make the dinner, so you need to send out a new set of invitations. You’ll
have to think of someone else to invite.
Start with your program from Exercise 3-4. Add a print() call at the end
of your program, stating the name of the guest who can’t make it.
Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still
in your list."""
guests = ["Ali", "Ibrar", "Nadeem"]
print("Guests are:", guests);
poped_guest = guests.pop(0)
guests.insert(0, "Iftikhar")
print(f"Unfortunately {poped_guest}, couldn't make it, so {guests[0]} will be joining us instead." )
print(f"Dear {guests[0]}, you are cordially invited to dinner tonight")
print(f"Dear {guests[1]}, you are cordially invited to dinner tonight")
print(f"Dear {guests[2]}, you are cordially invited to dinner tonight")
