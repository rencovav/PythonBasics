print("Python Loops")

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

user_name = input("What is your name?")
if user_name in names_list:
    print("Your name is popular")
else:
    print("You have a unique name!")

"""
● You have international spelling alphabet
○ d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india',
'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike',
'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec',
'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform',
'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
'z':'zulu'}
● Write code that will
○ Ask user name
○ Spell user's name
"""

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta',
'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india',
'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike',
'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec',
'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform',
'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
'z':'zulu'}
name = input("What is your name?").lower()
for i in name:
    print(f"{i} as {d[i]}")

"""
● Transpose following list using both nested loops and list comprehensions
a = [[1,2,3],
 [4,5,6],
 [7,8,9]]
To this list
b = [[1,4,7],
 [2,5,8],
 [3,6,9]]
 """

a = [[1,2,3],
 [4,5,6],
 [7,8,9]]

b = [[a[y][x] for y in range(len(a))] for x in range(len(a[0]))]
for row in b:
    print(row)

"""
● Create shopping list
● Using for and break write code that
○ Will ask for new item
○ Go through the list
○ If item is found then
■ Print item
■ Stop searching
○ If item is not found
■ Append item to the list
"""
shopping_list = ["Apples", "Vegetables", "Butter", "Milk", "Baking powder", "Socks"]

item = input("Item")
for i in shopping_list:
    if i == item:
        print(item)
        break
if item not in shopping_list:
    shopping_list.append(item)

"""
● Create list containing 5 numbers
○ Using list comprehensions create list where:
■ Each element is multiplied by itself
● E.g. 5 → 25
■ 'is my favorite number!' is added to each element of the
list'
● E.g. '5 is my favorite number!'
● Print both lists
"""
numbers_list = [1,2,3,4,5]
multiplied_list = [str(x*x) + " is my favorite number!" for x in numbers_list]
print(numbers_list)
print(multiplied_list)

"""
● Using list comprehensions write code that
○ Takes string as an input, e.g. seq = 'ACTGCTCAAG'
○ Creates list with positions where 'A' is occurring, e.g. pos
= [0, 7, 8]
○ Prints created list
○ Hint: use enumerate()
● BONUS task: come up with the second solution
"""

seq = 'ACTGCTCAAG'
list_of_occurence = []
for i, letter in enumerate(seq):
    if letter == "A":
        list_of_occurence.append(i)
print(list_of_occurence)


"""
● You have dictionary of points in competition
○ scores = {'John' : 10, 'Emily' : 35, 'Matthew' : 50}
○ Using dictionary comprehensions, create dictionary, where everyone gets triple
amount of points
"""

scores = {'John' : 10, 'Emily' : 35, 'Matthew' : 50}
scores_tripled = {score : scores[score] *3 for score in scores}
print(scores_tripled)