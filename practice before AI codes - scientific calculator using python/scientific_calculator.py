import math
# This is basically a calculator using classes and inheritance, the main class is the s_calc class
# which inherits the basic_calc class and all of the basic functions are in the basic class
# and additional funtions are in the parent class


class basic_calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    # Function to add two numbers

    def add(num1, num2):
        return num1 + num2

    # Function to subtract two numbers

    def subtract(num1, num2):
        return num1 - num2

    # Function to multiply two numbers

    def multiply(num1, num2):
        return num1 * num2

    # Function to divide two numbers

    def divide(num1, num2):
        return num1 / num2


class s_calc(basic_calc):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def fact(num1):
        print(
            f"Factorial for the number {num1} is : {math.factorial(num1)}")

    def power(num1, num2):
        print(
            f"Power of number {num1} raise to {num2} is : {int(math.pow(num1,num2))}")

    print("Please select operation -\n",
          "1. Add\n",
          "2. Subtract\n",
          "3. Multiply\n",
          "4. Divide\n",
          "5. Factorial\n")

    # Take input from the user
    select = int(input("Select operations form 1, 2, 3, 4, 5 :"))

    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if select == 1:
        print(number_1, "+", number_2, "=",
              basic_calc.add(number_1, number_2))

    elif select == 2:
        print(number_1, "-", number_2, "=",
              basic_calc.subtract(number_1, number_2))

    elif select == 3:
        print(number_1, "*", number_2, "=",
              basic_calc.multiply(number_1, number_2))

    elif select == 4:
        print(number_1, "/", number_2, "=",
              basic_calc.divide(number_1, number_2))
    elif select == 5:
        fact(number_1)
    elif select == 6:
        power(number_1, number_2)
    else:
        print("Invalid input")
