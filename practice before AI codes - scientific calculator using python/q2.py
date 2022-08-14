# this is a fibonacci series genrating question

second_previous = 0
previous = 1
current = 0
num = int(input("Enter the iterations number for fibonacci series : "))
print("fibonacci series for given input is : ", end="")
print(second_previous, " , ", previous, end="")
for i in range(1, num+1):
    current = second_previous+previous
    print(current, " , ", end="")
    second_previous = previous
    previous = current
