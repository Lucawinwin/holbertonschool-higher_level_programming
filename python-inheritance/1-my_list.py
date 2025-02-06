#!/usr/bin/python3
"""
Write a class MyList that inherits from list
    """


class MyList(list):
    """
    The class MyList, which inherits from the list, includes a method
    that prints the list sorted in ascending order.
    """

    def print_sorted(self):
        print(sorted(self))
