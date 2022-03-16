
class Cat:
    SPECIES_NAME = "Felis catus"

    def __init__(self, name, age):
        if name is None or len(name) == 0 or age < 0:
            raise ValueError("This ain't a right cat")
        self.__name = name
        self.__age = age

    def meow(self):
        print(f"meow i'm {self.__name} and i'm {self.__age}")

    @staticmethod
    def cat_to_human_years(cat):
        return cat.__age * 7


def main():
    monty = Cat("monty", 5)
    chihiro = Cat("chihiro", 3)

    # Object calling an instance method, execution unique to the object
    # Prints "meow i'm monty" or "meow i'm chihiro"
    monty.meow()
    chihiro.meow()

    # Will not work
    # self.name is an instance variable... but Cat is a class
    # So where would self.name be referenced?
    # Cat.meow()

    # Calling a static variable with the class name is standard
    print(Cat.SPECIES_NAME)

    # Can also call the static variable with an object belonging to the class
    # Can be confusing and usually not standard
    print(monty.SPECIES_NAME)

    # Static method have same rules
    print(Cat.cat_to_human_years(monty))

    try:
        Cat("", 0)
    except ValueError as e:
        print(e)

    try:
        Cat("n", -1)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
  main()
