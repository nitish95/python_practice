#Write a Python Program to find largest element in an array.

def find_largest_array(arr):
    if not arr:
        return "Array is empty."
    
    largest_array= arr[0]

    for element in arr:
        if element > largest_array:
            largest_array = element
    return largest_array

my_array = list(map(int,input("Enter the element in array: ").split()))

result= find_largest_array(my_array)
print(f"The largest element in array: {result}")