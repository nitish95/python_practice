#Write a Python Program to find sum of array.
# my_list = [1, 2, 3, 4, 5]

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(arr)

total = sum(arr)

print(total)