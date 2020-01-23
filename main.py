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


# if statements

check = False

if check == False:
    print("It is false")
elif check == "Hamburger":
    print("Yum Hammmys")
elif check == "Yo":
    print("Hello")
else:
    print("It is actually equal to true")

# For/ while loops
# for
numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print("This number is", str(item))

# while
run = True
current = 1

while run:
    if current == 100:
        run = False

    else:
        print(current)
        current += 1

# Importing libraries

# in python console
# import re (regex)
# string = "'I AM NOT YELLING', she said. Though, they knew it not to be true
# new = re.sub('[A-Z]', '', string)
# now string will not have caps
# new = re.sub('[a-z]', '', string)
# no more lower case
# First arguments are what you are selecting
# Second argument is for what you are replacing your selection with
# Third argument is for the string you are manipulating
# Multiple selections may be used eg. '[.,\'a-zA-Z]' will remove everything in this particular string except spaces
# To remove spaces as well '[.,\'a-zA-Z+" "]'
# string = string + "6 298 - 345"
# new = re.sub('[^0-9]', '', string) will remove everything EXCEPT numbers
