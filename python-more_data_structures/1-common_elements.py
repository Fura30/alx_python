def common_elements(set_1, set_2):
    # Initialize an empty set to store the common elements
    common_set = set()

    # Iterate through elements in set_1
    for elem in set_1:
        # Check if the element is present in set_2
        if elem in set_2:
            # If found, add it to the common_set
            common_set.add(elem)

    return common_set
