import os

def load_names():
    """
    Load the file names.txt and return a list with the names.

    This function searches for the names.txt file in the current directory and subdirectories.
    It reads the file line by line and returns the names as a list.

    Returns:
        list: A list of names read from the names.txt file.

    Raises:
        FileNotFoundError: If the names.txt file cannot be found in the directory tree.
    """

    # Search for the names.txt file in the current directory and subdirectories
    for root, dirs, files in os.walk('.'):
        if 'names.txt' in files:
            file_path = os.path.join(root, 'names.txt')
            break
    else:
        raise FileNotFoundError("names.txt file not found in the directory tree")

    # Open the file and read the contents line by line
    with open(file_path, 'r') as file:
        names = [line.strip() for line in file]

    return names
