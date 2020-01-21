# flexible number of arguments
def print_people(*people):
    for person in people:
        print("This person is", person)


print_people("Dylan", "Jack", "Lou", "Olivia")


# Return functions

def do_math(num1, num2):
    return num1 + num2


math1 = do_math(5,7)
math2 = do_math(11, 24)

print("First sum is", math1, "and the second sum is", math2)