# Separate Vowels and Consonants in a String

string = "hi hello raju"

vowels = ""
consonants = ""

for ch in string:
    if ch.isalpha():          # Check only alphabets
        if ch.lower() in "aeiou":
            vowels += ch
        else:
            consonants += ch

print("Vowels     :", vowels)
print("Consonants :", consonants)