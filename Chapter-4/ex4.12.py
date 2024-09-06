"""4-12. More Loops: All versions of foods.py in this section have avoided
using for loops when printing, to save space. Choose a version of
foods.py, and write two for loops to print each list of foods."""
foods1: list[str] = ["pizza", "burger", "sandwich"]
foods2: list[str] = ["macaroni", "halwa", "paneer"]
for food in foods1:
    print("foods in foods1: ",food)
for food in foods2:
    print("foods in foods2: ",food)