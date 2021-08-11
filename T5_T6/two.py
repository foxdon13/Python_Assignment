import sys


try:
    with open(sys.argv[1], "r") as file:
        print(file.read())
        flag = False
except FileNotFoundError:
    print("file not found, Please enter the file name again")
