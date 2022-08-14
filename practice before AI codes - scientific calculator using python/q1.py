# This is a program that inputs 2 integers and prints prime numbers between that range

print("Program to print prime numbers between given range")
lower_limit = int(input("Enter positive lower Limit : "))
upper_limit = int(input("Enter positive upper Limit : "))

print(f"prime numbers between {lower_limit} and {upper_limit} is : ")
for num in range(lower_limit, upper_limit+1):
    flag = False
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
        if flag != True:
            print(num)
