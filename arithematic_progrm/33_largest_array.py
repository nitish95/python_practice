#Write a Python Program to find largest element in an array.

arr = list(map(int,input("Enter the array: ").split()))
#arr = {1,2,23,12}
y= sorted(arr)
#x= list(arr)
print(arr)

x=int(len(arr))
#print(x)

print(y[x-1])
"""print(sorted(arr))

length = len(arr)
print(length)
print("largest element: ", + arr[3])"""