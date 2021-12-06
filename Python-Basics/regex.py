import re

#1
string = """
Agalma elegans
Frillagalma vityazi
Cordagalma tottoni
"""

match = re.sub('^([A-Z])[^ ]*(.*)', '\1.\2', string)
print(match)

#2
def getName():
   name = input("Enter your name: ")
   regex = r'[A-Z][a-zA-Z]*'
   if (re.fullmatch(regex, name)):
       return name
   else:
     print("Your name is invalid, please enter only letters and first one is uppercase")
     getName()

print(getName())

#3
def only_digits(string):
    return re.sub('[^0-9]', '', string)

numbers = '2004-595-559'
print(only_digits(numbers))

#4
file = './zen.txt'

def before_dot(string):
    return True if re.match(r'^[^.]*[ao].*\.', string) else False

def is_alphanumeric(string):
    return True if re.findall('.*[:alnum:].*', string) else False

def has_two_t(string, optional=''):
    return True if re.findall(f'[Tt].*[Tt]{optional}', string) else False

letter_before_dot_lines = 0
alphanumeric_lines = 0
two_t_lines = 0
one_to_two_t_lines = 0

with open(file) as zen:
    for line in zen:
        if before_dot(line):
            letter_before_dot_lines += 1
        if is_alphanumeric(line):
            alphanumeric_lines += 1
        if has_two_t(line):
            two_t_lines += 1
        if has_two_t(line, '?'):
            one_to_two_t_lines += 1

print(f'Number of lines with a or o before . (dot): {letter_before_dot_lines}')
print(f'Number of lines with alphanumeric characters: {alphanumeric_lines}')
print(f'Number of lines with two T (upper or lower case): {two_t_lines}')
print(f'Number of lines with one to two T (upper or lower case): {one_to_two_t_lines}')
