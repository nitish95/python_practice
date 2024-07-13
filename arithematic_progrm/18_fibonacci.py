#Write a Python Program to Print the Fibonacci sequence.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
# 𝐹(0) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛 − 1) + 𝐹(𝑛 − 2)𝑓𝑜𝑟𝑛 > 1

nlimit = int(input("Enter limit for fibonacci seq: "))
n1,n2 = 0,1
count=0

if nlimit <0:
    print("Enter a valid +ve limit.")
elif nlimit == 1:
    print(f"fibonacci seq: 0 1")
else:
    #print(f"Fibonacci seq to limit {nlimit}")
    while count < nlimit:
        print(f"Fibonacci {count}th seq to limit {n1}")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        


