"""4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop
to print the numbers in your list."""
multiples_3 : list = list(range(3,31,3))
for value in multiples_3:
    print(value)
print([value for value in range(3,31,3)])