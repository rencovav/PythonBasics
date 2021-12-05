"""
● Write script
● Input values: two strings (word and letter) as arguments from command line
● Script will print word without specified letter
● Example:
$python extract_letter.py python o
pythn
$python extract_letter.py python l
python
"""

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("word")
parser.add_argument("letter")

args = parser.parse_args()

word = args.word
letter = args.letter

for char in word:
    if char == letter:
        word = word.replace(letter, "")

print(word)