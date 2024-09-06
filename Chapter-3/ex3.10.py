"""3-10. Every Function: Think of things you could store in a list. For
example, you could make a list of mountains, rivers, countries, cities,
languages, or anything else you’d like. Write a program that creates a list
containing these items and then uses each function introduced in this
chapter at least once."""
guests = ['Asghar', 'Ali', 'Nosheen', 'Ibrar', 'Nadeem', 'Ibtisam', 'Radhika']
print("guests original: ", guests)
guests.append("Malika")
print("Malika appended, now guests are: ", guests)
guests.remove("Nadeem")
print("Nadeem removed, now guests: ", guests)
guests.insert(1,"Raheema")
print("Raheema inserted at index 1, now gurests:", guests)
del guests[2]
print("deleted guest at index 2, now guests:", guests)
guests.pop(-2)
print("Poped guest at index -2, now guests: ", guests)
guests.sort()
print("guests sorted: ", guests)
guests.reverse()
print("gurests reversed: ", guests)
print("guests sorted by sorted() method: ", sorted(guests))
print("guests sorted reversed by sorted reverse method: ", sorted(guests, reverse = True))
print(f"The length of guests is: {len(guests)}")




