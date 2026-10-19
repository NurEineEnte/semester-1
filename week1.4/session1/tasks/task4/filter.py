# Week 4, Session 1: 

# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?

# Your task is to update the docstring to reflect what the function does.


def filter_positive_numbers(numbers):
    """
    returns a new list of numbers from the original, only adding the positive valeus from the original list through a list comprehensino
    """
    return [num for num in numbers if num > 0]
