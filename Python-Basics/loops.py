"""
You have list of top 20 names in Czech Republic
● names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef',
'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav',
'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal',
'Lenka', 'Katerina']
● Write code that
○ Ask user for its name (reminder use: input(‘Your name’))
○ Check if name is in the list (reminder use: in)
■ If name is in the list then it prints reply
■ If name is not in the list then it prints another reply
"""

names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef',
'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav',
'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal',
'Lenka', 'Katerina']

print("What is your name?")
user_name = input()
for name in names_list:
    if user_name == name:
        print("Your name is popular")
    else:
        print("You have an unique name!")
