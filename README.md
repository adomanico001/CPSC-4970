# Module 2 Exercise & Project Description
**Exercise**

Create a module called `list_tools` (file named list_tools.py) and use list comprehensions to implement the following functions:

- `all_even(lst)` -- return a list of even numbers occurring in the list lst, in the same order as they appear in lst
- `all_not_multiple(lst, n)` -- return a list of the numbers in lst that are not multiples of n, in the same order as they appear in lst
- `max_from_2_tuples(tuples)` -- tuples is a list of 2-tuples.  Return a 2-tuple that contains the max of the first element of each tuple and the max of the second element of each tuple.  For example, max_from_2_tuples([(-1, 5), (13, 2)]) would return (13, 5).
- `lower_case_words(sentence)` -- return a list of words in sentence converted to lower case.  Do not include any empty strings in your result. Words are separated by one or more space characters.
- `baby_names(names, last_name)` -- names is a non-empty list of distinct strings, last_name is a string.  Return a list of "full names" containing all possible pairs of distinct names in names, with last_name appended (and a space between each part of the name).  For example baby_names(["Fred", "James"], "Smith") would return ["Fred James Smith", "James Fred Smith"].  See unit tests for more examples.
