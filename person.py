import numpy as np
import load_names

"""
Implements the Person class and a function for generating a list of Person instances.
Person class holds information about an individual's name, age, height, and weight.
create_people_list function is used to create a collection of Person instances with random data.
"""

# PERSON_NAMES holds an array of common first names.
PERSON_NAMES = load_names.load_names()  # Use global namespace conventions for constants.

class Person:
    """
    Represents a person with name, age, height, and weight attributes.
    """

    def __init__(self, name, age, height, weight):
        """
        Constructs a new Person instance.

        Args:
            name: Person's name.
            age: Person's age.
            height: Person's height in cm.
            weight: Person's weight in kg.
        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        """
        Formats the Person instance as a string.
        """
        return f"Person: {self.name}, Age: {self.age}, Height: {self.height} cm, Weight: {self.weight} kg"

    def __lt__(self, other_person):
        """
        Compares two Person instances based on height.

        Args:
            other_person: Another Person instance.

        Returns:
            True if this person is shorter, False otherwise.
        """
        return self.height < other_person.height

    def __eq__(self, other_person):
        """
        Checks if two Person instances have the same height.

        Args:
            other_person: Another Person instance.

        Returns:
            True if heights are equal, False otherwise.
        """
        return self.height == other_person.height

    # Accessor methods for attributes
    @property
    def get_name(self):
        return self.name

    @property
    def get_age(self):
        return self.age

    @property
    def get_height(self):
        return self.height

    @property
    def get_weight(self):
        return self.weight

    def as_tuple(self):
        return (self.name, self.age, self.height, self.weight)

    def as_list(self):
        return [self.name, self.age, self.height, self.weight]

    def __getitem__(self, idx):
        return (self.name, self.age, self.height, self.weight)[idx]

def create_people_list(number_of_people):
    """
    Generates a list of Person instances with random data.

    Args:
        number_of_people: The number of Person instances to generate.

    Returns:
        A list of Person instances.
    """
    list_of_people = []
    for _ in range(number_of_people):
        random_name = np.random.choice(PERSON_NAMES)
        random_age = np.random.randint(18, 101)
        random_height = np.random.randint(150, 201)
        random_weight = np.random.randint(45, 101)
        list_of_people.append(Person(random_name, random_age, random_height, random_weight))

    return list_of_people
