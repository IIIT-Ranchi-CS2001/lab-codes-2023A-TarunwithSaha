# Write a python script using map, lambda and filter functions to do the following operations on a user inputted comma separated strings: E.g.: “Tom 25 Rahu22 2@$” 
# To find all the letters given in the string and to convert them to uppercase
# o/p: [‘TOM’]
# To find all the digits present in the string and to find their squares
# o/p: [625]
# To display all the alphanumeric characters present in the string
# o/p: [“Tom”, ‘25’, “Rahu22”]


# User input of a comma-separated string
input_string = input("Enter a comma-separated string: ")

# Split the input string by commas and strip whitespace
items = [item.strip() for item in input_string.split(",")]

# Find all strings that contain only alphabetic characters and convert them to uppercase
letters_uppercase = list(map(lambda x: x.upper(), filter(lambda x: x.isalpha(), items)))

# Find all items that are digits and compute their squares
squared_digits = list(map(lambda x: int(x) ** 2, filter(lambda x: x.isdigit(), items)))

# Display all alphanumeric strings (contains both letters and numbers)
alphanumeric_items = list(filter(lambda x: x.isalnum(), items))

# Display the results
print("Uppercase Letters:", letters_uppercase)
print("Squared Digits:", squared_digits)
print("Alphanumeric Items:", alphanumeric_items)
