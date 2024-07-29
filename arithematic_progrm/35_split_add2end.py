#Write a Python Program to Split the array and add the first part to the end?


arr = list(map(int, input("Enter the array: ").split()))
n=len(arr)

arr1=[]
arr2=[]
arr3=[]

d1=int(n/2)
d2=int((n/2)+1)

#print("d1",+d1,"d2",+d2)
