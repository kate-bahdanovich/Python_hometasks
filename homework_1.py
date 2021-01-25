# import "random" module to get access to the random object (or whatever it is)
import random
# define a variable to store the list of the numbers
a = []
# define a variable to store and quick change of the length of the list
len = 100
# a cycle to generate 100 random numbers one by one
for i in range(len):
    # generate a number and add it to the list a
    a.append(random.randint(0,1000))


# 2 - sort algorithm implementation ("simple buble")
# declare flag for the end of the sorting
swapped = 1
# while we find elements to swap as we are going through array of numbers(new order of elements at each loop) "swapped" will be equal to 1
while swapped == 1:
    # clear "swapped" before a loop trough a list
    swapped = 0
    # loop trough a list. As we would compare two elements(this and the next one) at each step we should limit steps number to Length-1 = 99
    for i in range(len-1):
        # if we find elements to be swapped (the previous is larger then the next one)
        if a[i] > a[i+1]:
            # swapped them through a "temp" ...
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            # ... and change the outer cycle flag ( 1 => to continue sorting)
            swapped = 1


#   3 - calculate average for even and odd numbers
# declare variable to store a sum and a number of the odd values
s_odd = 0
n_odd = 0
# declare variable to store a sum and a number of the even values
s_even = 0
n_even = 0
# one more cycle through a list for averages calculation
for i in range(len):
    # condition to define if the list value is even or not
    if a[i] % 2 == 0:
        # value is even => increase the sum(by a value) and the number(by 1) of even values
        s_even = s_even + a[i]
        n_even = n_even + 1
    else:
        # value is odd => increase the sum(by a value) and the number(by 1) of odd values
        s_odd = s_odd + a[i]
        n_odd = n_odd + 1
# division by zero catching for odd values
try:
    average_odd = s_odd / n_odd
except ZeroDivisionError:
    average_odd = "not defined"
# division by zero catching for even values
try:
    average_even = s_even / n_even
except ZeroDivisionError:
    average_even = "not defined"

# 4 - print both average results in console. Round float results to 3 digits after point
print("The average for the odd values is:", round(average_odd,3))
print("The average for the even values is:", round(average_even,3))