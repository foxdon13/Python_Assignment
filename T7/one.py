import math

C = 50
H = 30
user_input = input("Enter the value of D in a comma-seperated sequence ")
D = list(map(lambda x: int(x), user_input.split(",")))
for value in D:
    Q = math.sqrt(((2 * C * value) / H))
    print(f"square root is : {Q}")
