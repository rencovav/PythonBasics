

with open("list_of_things.txt", "w", encoding="utf-8") as file:
    my_things = ["casserole", "book", "knife", "water bottle", "fishing rod"]
    for i in range(len(my_things)):
        print(str(i+1) + "\t" + my_things[i])
