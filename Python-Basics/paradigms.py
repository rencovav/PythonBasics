class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.__purr_sound = "Purr Purr Purr"

    def purr(self):
        print(self.__purr_sound)


cat = Cat("Micka")
print(cat.get_name())
cat.purr()
