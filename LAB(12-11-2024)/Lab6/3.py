# Write program to define a function my_max() to complete the following tasks: [Usage of built-in function max() is strictly prohibited]
# If a list of integers is passed as the input argument, the function shall return maximum value present in the list
# If a set is passed, maximum value present in the list
# If a tuple is passed, maximum value present in the tuple
# Hint: Pass the container type unpacked using *
def my_max(*args):
    # Initialize the max_value with the first element of args
    max_value = args[0]
    # Iterate over all elements in args
    for value in args:
        if value > max_value:
            max_value = value
    return max_value
