with open("doc.txt", "r") as f:
    content = f.readlines()
    for line in content:
        if len(line):
            print(line)
