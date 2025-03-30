# Single Line comment
# Single Line comment
# Single Line comment

"""Multi
Line
Comment"""

'''Multi
Line
Comment'''

# print(10)


# DocString In Python, docstring refers to documentation string. A docstring is included as a first-line inside a function, module, class or method. Docstring is a short description of what your function, module or class does.
# We write docstrings inside triple quotes.
def function(n):
    """
    The function returns n + 1 and prints the result.
    """
    result = n + 1
    return result

# To see the output, you should call the function and print its result
# Convert the result to a string before concatenation
print("This is the output of the function: " + str(function(6)))
print(function.__doc__)
