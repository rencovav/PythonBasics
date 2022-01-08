def positive_sum(in_list):
    """Adds together the members of a list.
 Args:
 in_list (list): List of positive numbers.

 Returns:
 int, float: Depending on the input numbers, returns the sum of them.

 Raises:
 TypeError: In case the in_list is not a list.
 ValueError: In case the any number in the list is negative.
 """
    if not type(in_list) == list:
        raise TypeError("The input is supposed to be list.")
    if any([x < 0 for x in in_list]):
        raise ValueError("The list members are supposed to be non-negative.")
    return sum(in_list)
