"""
Write script
● Input values: two strings as arguments from command line
● Script will print number of occurrences of substring in string
● Example:
$python count_occurrence.py ab abcdabcc
String ab occurred 2 times in string abcdabcc
"""

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("substring")
parser.add_argument("string")
args = parser.parse_args()

occurrence = args.string.count(args.substring)

print(f"String {args.substring} occurred {occurrence}x in string {args.string}.")