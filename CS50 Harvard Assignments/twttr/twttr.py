# ask the user for an input
word = input("Input: ")
vowels = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]
removed_vowels = ""
# remove the vowels
for letters in word:
    if letters not in vowels:
        removed_vowels += letters
print("Output: " + removed_vowels)