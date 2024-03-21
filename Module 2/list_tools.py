# This program aims to use list comprehensions to implement functions
#
# Module 2 Project
# @author - Addie Domanico - CPSC4970 - AO3
# @version - 03/24/2024


# Returns a list of even numbers occurring in lst
def all_even(lst):
    return [num for num in lst if num % 2 == 0]
lst = [1, 2, 3, 4]
print(all_even(lst))


# Returns a list of numbers in lst that are not multiples of n
def all_not_multiple(lst, n):
    return [num for num in lst if num % n != 0]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
print(all_not_multiple(lst, n))


# Returns a 2-tuple that contains the max element of each tuple
def max_from_2_tuples(tuples):
    if not tuples:
        return None
    max_first = max(t[0] for t in tuples)
    max_second = max(t[1] for t in tuples)
    return max_first, max_second
tuples = [(-1, 5), (13, 2)]
print(max_from_2_tuples(tuples))


# Returns a list of words converted to lower case
def lower_case_words(sentence):
    words = sentence.split()
    return [word.lower() for word in words if word.lower()]
sentence = "The Quick Brown FOX Jumps Over The Lazy DOG"
print(lower_case_words(sentence))


# Returns a list of "full names"
def baby_names(names, last_name):
    return [f"{first} {second} {last_name}" for i, first in enumerate(names) for j, second in enumerate(names)
            if i != j]
names = ["Ben", "Jerry"]
last_name = "Smith"
print(baby_names(names, last_name))
