import os

folders= str(input("Enter the folder path: ")).split()

for folder in folders:

    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print("File not available."+folder)
        break

    print("===== list of file in the folder: ")

    for file in files:
        print(file)

