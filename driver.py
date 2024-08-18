import numpy as np
import load_names
from merge_sort import merge_sort
from person import Person, create_people_list

def run_person_sorter():
    people_list = []  # List to store Person objects

    while True:
        print("\n=== Person Management System ===")
        print("[1] Generate Random People")
        print("[2] Organize People")
        print("[3] Close Program")
        user_input = input("Select an option: ")

        if user_input == "1":
            count = int(input("Number of people to generate: "))
            people_list = create_people_list(count)
            print("\nGenerated People:")
            for individual in people_list:
                print(f"Person: {individual} -> Details: {individual.as_tuple()}")

        elif user_input == "2" and people_list:
            print("Choose sorting criteria:")
            print("a. Height")
            print("b. Age")
            print("c. Weight")
            print("d. Name")
            sort_option = input("Sorting choice: ")

            reverse_order = input("Sort in descending order? (yes/no): ").lower() == 'yes'

            criteria_map = {
                "a": "height",
                "b": "age",
                "c": "weight",
                "d": "name"
            }

            sort_function_map = {
                "a": lambda person: person.height,
                "b": lambda person: person.age,
                "c": lambda person: person.weight,
                "d": lambda person: person.name
            }

            if sort_option in sort_function_map:
                organized_people = merge_sort(people_list, sort_key=sort_function_map[sort_option], descending= reverse_order)
                print(f"\nPeople organized by {criteria_map[sort_option].capitalize()} {'(Descending)' if reverse_order else ''}:")
                for individual in organized_people:
                    print(f"Person: {individual} -> {criteria_map[sort_option].capitalize()}: {getattr(individual, criteria_map[sort_option])}")
            else:
                print("Invalid sorting option.")
        elif user_input == "3":
            print("Shutting down the system.")
            break
        else:
            print("Invalid input, please try again.")

        if not people_list:
            print("No people data available. Please generate data first.")

if __name__ == "__main__":
    run_person_sorter()
