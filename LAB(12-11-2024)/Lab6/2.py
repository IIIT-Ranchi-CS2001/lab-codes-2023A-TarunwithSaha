#Define a function my_sort() to sort the list of tuples created using my_zip function in the last question. The function must have two types of arguments- the list that carry the data, the key that determines the argument of sorting:
# [Usage of built-in function sorted() is a punishable offense]
# Key = 0: sorting based on customer name in ascending order
# Key = 1: sorting based on Customer ID
# Key = 2: sorting based on shopping points

def my_sort(data, key=0):
    # Bubble sort implementation
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            # Sorting by key
            if data[j][key] > data[j + 1][key]:
                # Swap elements if they are in the wrong order
                data[j], data[j + 1] = data[j + 1], data[j]
    return data
data=[1,2,3,4]
print(data)
my_sort(data)
print(data)
    