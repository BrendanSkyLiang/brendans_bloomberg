def find_common_set(list1, list2):
    """
    Finds all common values between two lists using sets.

    Args:
    list1: The first list.
    list2: The second list.

    Returns:
    A list of all common values, or an empty list if no common value is found.
    """
    common = set(list1) & set(list2)
    common_values = list(common)
    if len(common_values) == 0:
        raise ValueError(f"no common values")
    else:
        return common_values