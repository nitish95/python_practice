#Write a script that reads a file line by line and counts the number of lines containing a specific word. (use file handling with open() and readline() methods)

with open('/home/nitishjoshi/Documents/python example/Gemia_questions/text_file.txt','r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total number of lines: ', count+1)