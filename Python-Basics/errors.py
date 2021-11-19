"""
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[4])
"""

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[3])

"""
for number in range(10):
 # use a if the number is a multiple of 3, otherwise use b
 if (Number % 3) == 0:
 message = message + a
 else:
 message = message + "b"
print(message)
"""

for number in range(10):
 # use a if the number is a multiple of 3, otherwise use b
    message = ""
    if (number % 3) == 0:
        message = message + "a"
    else:
        message = message + "b"
print(message)

"""
● Ask user to type name
● Raise exception if name
○ Contains number
○ Has spaces
○ Does not start with uppercase letter
"""

user_name = input("Type a name")
if user_name:
    for char in user_name:
        if char.isdigit():
            raise Exception("Contains number")

if user_name.__contains__(" "):
    raise Exception("Has spaces!")
if user_name[0].islower():
    raise Exception("Does not start with uppercase letter")

"""
Exercise
● Create function that ask user to type two integers and
return division result
● If user type other data type than integer, ask to type
integer
● If second number is 0, ask user to type number again until
number is not 0
● Hint: while and/or try - except 
"""

input_ok = False
result = 0
while not input_ok:
    x = (input("Enter x"))
    y = (input("Enter y"))

    try:
        result = int(x) / int(y)
        input_ok = True

    except ZeroDivisionError:
        print("Division by zero is not possible, enter another number")
    except ValueError:
        print("Enter an integer")

print(result)

"""
year == int.input("Greetings! What is your year of origin? '))
if year <= 1900
 print ('Woah, that's the past!')
elif year > 1900 && year < 2020:
 print ("That's totally the present!")
elif:
 print ("Far out, that's the future!!")
"""

year = int(input("Greetings! What is your year of origin? "))
if year <= 1900:
    print('Woah, that\'s the past!')
elif (year > 1900) and (year < 2020):
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")