#Print the runner-up score.

if __name__ == '__main__':
    n = int(input())
    arr= []
    for i in range(n):
        value = int(input(f"Enter value{i+1}: "))
        arr.append(value)
        print(f"append{arr}")
        
        arr.sort(reverse=True)
        print(f"sorted array {arr}")
    
    for x in range(n):
        if arr[x] != arr[x+1]:
              print(f"runner up", arr[x+1])
                                