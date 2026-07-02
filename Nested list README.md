PYTHON NOTES

1. LIST
Definition:
A List is an ordered, mutable (changeable) collection that allows duplicate values.

Syntax:
list_name = [value1, value2, value3]

Example:
fruits = ["Apple", "Banana", "Mango"]
print(fruits)

Features:
• Ordered
• Mutable
• Allows duplicates
• Indexed
• Stores different data types

------------------------------------------------------------

2. NESTED LIST
Definition:
A Nested List is a list that contains one or more lists as its elements.

Syntax:
nested_list = [[1,2],[3,4],[5,6]]

Example:
students = [["Raju",90],["Anu",85],["Ravi",95]]

print(students)
print(students[0])
print(students[1][1])

Features:
• List inside another list
• Uses multiple indexes
• Used for matrix/table representation

------------------------------------------------------------

3. TUPLE
Definition:
A Tuple is an ordered and immutable (cannot be changed) collection.

Syntax:
tuple_name = (value1, value2, value3)

Example:
numbers = (10,20,30)

print(numbers)
print(numbers[1])

Features:
• Ordered
• Immutable
• Allows duplicates
• Indexed
• Faster than list

------------------------------------------------------------

4. SET
Definition:
A Set is an unordered collection of unique elements.

Syntax:
set_name = {value1, value2, value3}

Example:
numbers = {10,20,30,20}

print(numbers)

numbers.add(40)
print(numbers)

Features:
• Unordered
• Mutable
• No duplicate values
• Not indexed

------------------------------------------------------------

5. DICTIONARY
Definition:
A Dictionary stores data as Key : Value pairs.

Syntax:
dict_name = {
    "key1": value1,
    "key2": value2
}

Example:
student = {
    "Name":"Raju",
    "Age":20,
    "Marks":95
}

print(student)
print(student["Name"])

Features:
• Key-Value pairs
• Mutable
• Keys are unique
• Values can be duplicated

------------------------------------------------------------

DIFFERENCE

Feature         List        Tuple       Set         Dictionary
----------------------------------------------------------------
Syntax          []          ()          {}          {key:value}
Ordered         Yes         Yes         No          Yes
Mutable         Yes         No          Yes         Yes
Duplicates      Yes         Yes         No          Keys-No
Indexed         Yes         Yes         No          By Key

------------------------------------------------------------

SUMMARY

List        -> Ordered, Mutable, Duplicates Allowed
Nested List -> List inside another List
Tuple       -> Ordered, Immutable
Set         -> Unordered, Unique Elements
Dictionary  -> Key-Value Pair Collection
