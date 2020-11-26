# Stuff I've learned
# ==================

from turtle import Turtle

# The Problem:
#   I want to find the index of the item
#   with the minimum values of x and y
#   in the example list of dictionaries

# Example of list of dictionaries
snake_body = [
    {'seg': Turtle(), 'x': 0, 'y': 10},
    {'seg': Turtle(), 'x': -20, 'y': 0},
    {'seg': Turtle(), 'x': 20, 'y': -20},
    {'seg': Turtle(), 'x': -20, 'y': -20},
]


def min_value():
    # https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-15.php
    # Not quite what I'm after. This only returns the (first) minimum values found.
    """Make a list out of x and y positions,
    then find minimum of list"""
    list_x = [a["x"] for a in snake_body]
    list_y = [a["y"] for a in snake_body]
    min_x = min(list_x)
    min_y = min(list_y)
    print("Results from min_value()")
    print(f"list_x = {list_x}, list_y = {list_y}")
    print(f"min_x = {min_x}, min_y = {min_y}")
    print()


def min_item():
    # https://stackoverflow.com/questions/5320871/in-list-of-dicts-find-min-value-of-a-common-dict-field
    # Better. This returns the entire item of the (first) lowest item found.
    min_x = min(snake_body, key=lambda x: x["x"])
    min_y = min(snake_body, key=lambda y: y["y"])
    print("Results from min_item()")
    print(f"min_x = {min_x}, min_y = {min_y}")
    print()


def min_index():
    # https://stackoverflow.com/questions/30546889/get-max-value-index-for-a-list-of-dicts
    # This is what I need - returns the INDEX to the (first) lowest item found.
    # I'm still not quite sure how it works though!
    min_x = min(range(len(snake_body)), key=lambda index: snake_body[index]['x'])
    min_y = min(range(len(snake_body)), key=lambda index: snake_body[index]['y'])
    print("Results from min_index()")
    print(f"min_x = {min_x}, min_y = {min_y}")
    print()


min_value()
min_item()
min_index()
