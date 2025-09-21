class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self._species = species
        self.__age = age

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if value.strip():
            self._species = value
        else:
            raise ValueError("Species cannot be empty")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__age = value
        else:
            raise ValueError("Age must be a non-negative number")

    def __str__(self):
        return f"{self.name} ({self._species}), {self.__age} years old"


if __name__ == "__main__":
    dog = Animal("Buddy", "Dog", 3)

    print(dog.name)
    dog.name = "Max"

    print(dog.species)
    dog.species = "Canine"

    print(dog.age)
    dog.age = 4

    print(dog)

