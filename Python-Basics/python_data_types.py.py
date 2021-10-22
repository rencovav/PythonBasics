import datetime

print("Dobrý den")

"""Exercise
The king with lots of children got heritage - 1256983
golden coins. He decided that he will divide his heritage
evenly among all of his 28 children. How many coins will
remain to him?
"""

heritage = 1256983
children = 28

print(heritage % children)
print("7 coins will remain to the king.")

"""
Exercise
● Evaluate if following is true
○ Remainder after division of 1252 by 15 is less than 8 or 3^5 is more than 100
○ 5 times 33 is not equal to 900 divided by 75
"""

print(1252 % 15 < 8 or 3**5 > 100)
print(5 * (3**3) != 900/75)

"""
Exercise
● Create one string from the 2 following strings:
○ '[[]]' + 'PYTHON ' → '[[PYTHON]]'
● Create one string from another
○ 'Python' → 'onononon'
○ 'Perl' → 'rrrrrr'
"""
cover = "[[]]"
content = "PYTHON"
print(cover[:2] + content + cover[2:])

print("python"[4::]*4)
print("Perl"[2:3]*6)

"""
Exercise
● Make first half of the string uppercase and second half lowercase
○ E.g. 'python' ---> 'PYThon'
● Create string which is first letter of another string repeated n
number of times, where n - length of the given string
○ E.g. 'python' ---> 'pppppp'
○ 'git' ---> 'ggg'
"""
text = "python"
print(text[0:3:1].upper() + text[3::1].lower())

print(text[0:1]*len(text))

"""
Exercise
● What results do you get when you run following expressions?
○ print(7+3*2)
○ print('7' + str(3*2))
○ print('7' + '3*2')
○ print('7' + 3*2)
● What is causing error ?
  The values are of a different data type and cannot be concatenated or summed up
"""

"""
Exercise
● Save your hobby to the 'hobby' variable 
○ Using format method print following string 'My hobby
is <your hobby>.' with completed hobby
● Transform variable date = '2018-11-01' to '01/11' using
format
"""

hobby = "reading"
print("My hobby is {0}.".format(hobby))
date = datetime.datetime.strptime("2018-11-01", "%Y-%m-%d")
print("{:%d/%m}".format(date))

"""
Exercise
● Create list of your hobbies by adding elements to the
empty list (the favourite one will be the first)
● Print the hobby you like most
● Print the hobby you like least
● Delete it
"""
my_list = []
my_list.append("reading")
my_list.append("programming")
my_list.append("studying")
print(my_list[1])
print(my_list[2])
my_list.remove(my_list[2])
print(my_list)

"""
Exercise
● List of the Czech cities sorted by population size
○ cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske
Budejovice', 'Pardubice']
● Sort cities in alphabetical order
● Using "".join() join cities into one string separated by asterisk (*)
"""
cities = ['Prague', 'Brno', 'Ostrava', 'Plzen', 'Liberec', 'Olomouc', 'Usti nad Labem', 'Hradec Kralove', 'Ceske Budejovice', 'Pardubice']
cities.sort()
print(cities)
all_cities = "*".join(cities)
print(all_cities)

"""
Exercise
alphabet = 'abcdefghijklmnopqrstuvwxyz'
zen = 
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!' 
'
● Find what letters are not present in the Zen of Python
● Hint: use set()
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

alphabet_set = set(alphabet)
zen_set = set(zen)
print(alphabet_set - zen_set)


"""
Exercise
● Fix dictionary and delete erroneous key
○ d = {'payton':'An interpreted, object-oriented programming language'}
● Use one of the data types and create dictionary, where key will be name and surname (do not put it at one string) and
value will be telephone number
"""

d = {'payton': 'An interpreted, object-oriented programming language'}
del d['payton']

dictionary = {("Vlasta", "Rencova"): 123456789}

"""
Exercise
● You have a dictionary
○ info = {('Name', 'Surname'):('John', 'Doe')}
● Extract dictionary value in following format
○ 'John_Doe'
"""

info = {('Name', 'Surname'): ('John', 'Doe')}

value = "{0}_{1}".format(info.get(("Name", "Surname"))[0], info.get(("Name", "Surname"))[1])
print(value)
