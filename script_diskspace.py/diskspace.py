import os

# Define the command to execute
command = "ls -l |grep -i 'rwx'"

# Execute the command (no output capture)
os.system(command)