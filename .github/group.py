def groups_of_3(values:list[int]) -> list[list[int]]:
    """
    Groups the elements of the input list into sublists of three elements each.
    The last sublist may contain fewer than three elements if there are not enough values.

    Input
    - values: A list of integers to group

    Output
    - result: A list of sublists, each containing up to three integers
    """
    result = [values[i:i+3] for i in range(0, len(values), 3)]
    return result
