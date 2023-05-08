# Alexander Hopfgartner

# TODO 1. Exercise 1: Famous Quote
# Find a quote from a famous person you admire. Write a function named famous_quote() that
# prints the quote and the name of its author.

def famous_quote():
    print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")


# famous_quote()

# TODO 2. Exercise 2: Number Eight
# Write a function called number_eight(), that uses addition, subtraction, multiplication, division
# and exponentiation operations that each result in the number 8. Be sure to enclose your operations
# in print() calls to see the results. Your function should include five lines that look like this:

def number_eight():
    print(5+3)
    print(10-2)
    print(4*2)
    print(int(16/2))
    print(2**3)


# number_eight()

# TODO 3. Exercise 3: Formatting
# Write a function name_age() that accepts the name and age of a person. It then prints it on the
# console in the following format:

def name_age():
    name = input("Please enter your name:\n")
    age = int(input("Please enter your age:\n"))

    print(f"Hello, {name}. You are {age} years old.")
    print("Hello, {0}. You are {1} years old.".format(name, age))
    print("Hello, " + name + ". You are " + str(age) + " years old.")


# name_age()

# TODO 4. Exercise 4: Swap
# Write a function swap_integers() that reads two integers from the user and prints them on the
# console. Then the function swaps the integers in memory and prints the swapped integers again on
# the console. If, for example, the first integer is x=10 and the second is y=20, x must have the value
# 20 after the swap (Hint: you can use a temporary variable). The function does not return anything.

def swap_integers():
    x = int(input("Please enter x: "))
    y = int(input("Please enter y: "))
    print(f"x={x}\ny={y}")
    z = x
    x = y
    y = z
    print(f"x={x}\ny={y}")


# swap_integers()

# TODO 5. Exercise 5: Modulo check
# Write a function check_numbers(number1, number2) that accepts two arguments. The
# function checks if any of the numbers is divisible by 6 and if both are divisible by 10. The function
# does return true if both conditions are true. Hint: Use the modulo operator.

def check_numbers(number1: int, number2: int) -> bool:
    if number1 % 6 == 0 or number2 % 6 == 0:
        return number1 % 10 == 0 and number2 % 10 == 0
    return False


# print(check_numbers(10, 60))

# TODO 6. Exercise 6: Summarizer
# Write a function sum_up(number1, number2) that accepts two integers and sums up every
# integer between the two numbers including the given integers (inclusive). Check if the second
# number is greater than the first and display a message if it’s not. The function returns the result as an
# integer.

def sum_up(number1: int, number2: int) -> int:
    return sum([x for x in range(number1, number2 + 1)])


# print(sum_up(2, 6))

# TODO 7. Exercise 7: Sequencer
# Write a function sequence(number) that accepts an integer as argument. It then checks if the
# given number is an integer between 0 and 9 (inclusive) and prints an error message if it’s not. In case
# the given number is between 0 and 9, the function prints the sequence of number from 0 to 9 on the
# console without the given number. The function does not return anything.

def sequence(number):
    if number in [x for x in range(0, 10)]:
        print(" ".join([str(num) for num in range(0, 10) if num != number]))
    else:
        raise Exception("The Error you wanted.")


# sequence(7)

# TODO 8. Exercise 8: String check
# Write a function check_string(text) that accepts a string and checks if it begins OR ends with
# the character “a”. Use built-in string methods of python. A list with all methods can be found here:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# The function returns True if the string begins or ends with an “a”. The function should work for
# lower and upper case strings.

def check_string(text: str) -> bool:
    return text.lower().endswith("a") or text.lower().startswith("a")


# print(check_string("MILCHA"))

# TODO 9. Exercise 9: ASCII Art
# Write a function triangle(rows) that accepts an integer and prints out a triangle of stars with
# spaces in between them with the height of the given integer.

def triangle(rows: int):
    [print("*" * x) for x in range(1, rows + 1)]


# triangle(8)
