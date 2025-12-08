# TASK 1: Create list function min_max that returns a tuple.
# The parametres in list can be float or int: min_max(nums: list[float | int])
# Tuple contain the min and max value of functon.
# Values in tuple can be only float, int or float or only int: tuple[float | int, float | int].
def min_max(
    nums: list[float | int],
) -> tuple[float | int, float | int]:  # Function created
    if not nums:  # if not numbers
        raise ValueError(
            "List can not be empty"
        )  # Show the ValueError: List can not be empty
    return (min(nums), max(nums))  # Otherwise, return the tuple (min, max)


##################################################################################################
# TASK 2: Create a function that return the list in organized items, from min to max.
# The parametres in list can be float or int: unique_sorted(nums: list[float | int])
# Items in organized List can be float or int: list[float | int].
def unique_sorted(nums: list[float | int]) -> list[float | int]:  # Function created
    return sorted(
        set(nums)
    )  # Return new ordenated list, with unique values (set "unduplicate" duplicated itens).


##################################################################################################
# TASK 3: Create a function that return a unique list.
# The parametres in list can be list or tuple: flatten(mat: list[list | tuple])
def flatten(
    mat: list[list | tuple],
) -> list:  # creating function with returnig a unique list.
    flat_list = []  # New list, to "join" list and tuple
    for element in mat:  # loop to pu all the lists/tuple in just one list.
        if (
            type(element) == list or type(element) == tuple
        ):  # verify fi it's a list/tuple
            flat_list.extend(element)  # If True: add itens to "var"
        else:
            raise TypeError(
                "The element or line is not a list or tuple"
            )  # Otherwise, return ERROR
    return flat_list  # Return thenew list


if __name__ == "__main__":
    print(min_max([42, -1, 3, 42]))
    print(unique_sorted([-1, -1, 0, 2, 2, 4]))
    print(flatten([[1, 2], (3, 4), [5]]))
