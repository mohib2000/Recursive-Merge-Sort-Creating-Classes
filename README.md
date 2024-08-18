The problem statement for the project is defined here: https://joshhug.github.io/LeidenITP/assignments/assignment4/
# Recursive MergeSort & Creating-Classes
Project Description

This project is a comprehensive Python implementation that addresses the problem statement from Assignment 4 of Leiden ITP. The assignment focuses on the efficient sorting and management of a list of Person objects using a recursive merge sort algorithm. The project demonstrates the integration of object-oriented programming with algorithmic design.
Project Structure:

    driver.py: The main script that ties all components together. It loads a list of names, creates Person objects, and sorts them using the merge sort algorithm.

    merge_sort.py: This module contains the recursive implementation of the merge sort algorithm. It handles sorting of both basic data types (like integers) and custom objects, specifically Person objects. The algorithm is designed to maintain stability while ensuring O(n log n) performance, making it suitable for large datasets.

    load_names.py: Responsible for loading names from the names.txt file and creating Person objects. Each Person object is assigned attributes such as age, height, and weight, which can be used as keys for sorting. This module ensures that the data is properly formatted and ready for sorting.

    person.py: Defines the Person class, which encapsulates attributes such as name, age, height, and weight. This class includes comparison methods (__lt__, __eq__, etc.) that enable sorting based on different attributes. The class structure allows for easy extension and customization for various sorting needs.

    names.txt: A text file containing a list of names. This file serves as the input data for the project. The names are read by load_names.py, which then creates Person objects from these names.

Features:

    Custom Sorting: The merge sort implementation can be customized to sort Person objects based on different attributes, such as name, age, height, or weight. The sorting order (ascending or descending) can also be easily adjusted.

    Efficiency and Stability: The merge sort algorithm used in this project is both efficient (O(n log n)) and stable, meaning it preserves the relative order of records with equal keys.

    Object-Oriented Design: The project demonstrates the power of object-oriented programming in Python, using classes and methods to encapsulate data and functionality. The Person class serves as a blueprint for creating complex objects that can be easily managed and manipulated.

    Extensibility: The modular design of the project allows for easy extension. Additional attributes or methods can be added to the Person class, and the sorting algorithm can be modified to accommodate new sorting criteria.

Usage:

To use this project, ensure all the Python scripts and the names.txt file are in the same directory. Run the driver.py script to load the names, create Person objects, and sort them using the merge sort algorithm. The sorted list can be further processed or outputted as needed.

