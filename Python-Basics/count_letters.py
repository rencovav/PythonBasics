"""
Write a small Python script count_letters.py using argparse that:
- Has a positional argument of the string in which letters are supposed to be
counted.
- Has two optional arguments:
- v: to count only vowels
- c: count only consonants
The script prints out a list of letters in alphabetical order with the number of
occurrences:
a 2
b 5
"""

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("letters")

parser.add_argument("--vowels", action="store_true")
parser.add_argument("--consonants", action="store_true")
args = parser.parse_args()

count_letters = len(args.letters)

if args.vowels or args.consonants:
    string = args.letters.lower()
    count_vowels = 0
    count_consonants = 0
    letters = {}
    for letter in string:
        if letter in "aeiouy":
            count_vowels += 1

        elif letter in "qwrtpsdfghjklzxcvbnm":
            count_consonants += 1

        letters[letter] = string.count(letter)

letters_individual = letters.items()
sorted_letters = sorted(letters_individual)

print(sorted_letters)




