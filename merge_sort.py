

def merge_sort(input_list, sort_key=None, descending=False):
    """
    Sorts a list using merge sort algorithm.

    Args:
        input_list: List to be sorted.
        sort_key: Function to determine the sorting criteria.
        descending: Sort in descending order if True.

    Returns:
        A sorted list.
    """
    # A list with one or no elements is already sorted
    if len(input_list) <= 1:
        return input_list

    # Divide the list into two parts
    middle = len(input_list) // 2
    left_half = merge_sort(input_list[:middle], sort_key, descending)
    right_half = merge_sort(input_list[middle:], sort_key, descending)

    # Combine the sorted halves
    return combine(left_half, right_half, sort_key, descending)

def combine(left_part, right_part, sort_key, descending):
    """
    Combines two sorted sublists into one sorted list.

    Args:
        left_part: The left sorted sublist.
        right_part: The right sorted sublist.
        sort_key: Function to determine the sorting criteria.
        descending: Combine in descending order if True.

    Returns:
        A combined and sorted list.
    """
    combined_list = []
    while left_part and right_part:
        # Use sort_key function on the first element of each sublist if provided
        left_element = left_part[0] if sort_key is None else sort_key(left_part[0])
        right_element = right_part[0] if sort_key is None else sort_key(right_part[0])

        # Decide which element to append based on the sorting order
        if (left_element < right_element and not descending) or (left_element > right_element and descending):
            combined_list.append(left_part.pop(0))
        else:
            combined_list.append(right_part.pop(0))

    # Add the remaining elements
    combined_list.extend(left_part if left_part else right_part)

    return combined_list