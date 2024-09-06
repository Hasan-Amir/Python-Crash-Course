"""5-2. More Conditional Tests: You don’t have to limit the number of tests
you create to 10. If you want to try more comparisons, write more tests
and add them to conditional_tests.py. Have at least one True and one False
result for each of the following:
Tests for equality and inequality with strings
Tests using the lower() method
Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
Tests using the and keyword and the or keyword
Test whether an item is in a list
Test whether an item is not in a list"""
str1: str= "Hello"
str3: str = "hellO"
str2: str = "World"
print(str == str1)
print(str == str2)
print(str != str1)
print(str != str2)
print(str1.lower() == str3.lower())
num1: int = 1
num2: int = 2
print( num1 == num2 )
print( num1 != num2 )
print( num1 >= num2 )
print( num1 >= num2 )
print( num1 > num2 )
print( num1 < num2 )
print( num1 == 1 and num2 > 1)
print( num1 < 1 or num2 > 1)
fruits : list[str] = ["apple", "mango", "apricot"]
print("mango" in fruits)
print("keto" in fruits)