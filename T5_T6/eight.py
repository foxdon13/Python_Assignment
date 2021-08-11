name = "Consultadd Training"


def reverse(name):
    for i in range(len(name) - 1, -1, -1):
        yield name[i]


reversed = ""
for i in reverse(name):
    reversed = reversed + i

print(reversed)
