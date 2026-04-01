"""
swap_examples.py

Demonstrates different ways to swap values in Python.
"""

def swap_using_tuple(a, b):
    """Swap using Python tuple unpacking"""
    a, b = b, a
    return a, b


def swap_using_temp(a, b):
    """Swap using a temporary variable"""
    temp = a
    a = b
    b = temp
    return a, b


def swap_list_elements(lst, i, j):
    """Swap elements in a list at index i and j"""
    lst[i], lst[j] = lst[j], lst[i]
    return lst


def main():
    print("=== Swap Using Tuple Unpacking ===")
    a, b = 5, 10
    print(f"Before swap: a = {a}, b = {b}")
    a, b = swap_using_tuple(a, b)
    print(f"After swap:  a = {a}, b = {b}\n")

    print("=== Swap Using Temporary Variable ===")
    a, b = 15, 20
    print(f"Before swap: a = {a}, b = {b}")
    a, b = swap_using_temp(a, b)
    print(f"After swap:  a = {a}, b = {b}\n")

    print("=== Swap List Elements ===")
    arr = [1, 2, 3, 4]
    print(f"Before swap: {arr}")
    arr = swap_list_elements(arr, 0, 2)
    print(f"After swap:  {arr}")


if __name__ == "__main__":
    main()