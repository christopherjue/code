# 1. Problem 5c: Fibonacci_Sequence.py Write a Python program to generate the Fibonacci sequence up to a given number of terms.
h = int(input("how many terms of the Fibonacci sequence do you want:   "))
my_list =list() # []
my_list.append(0) # [0]
my_list.append(1) # [0,1]


for i in range(1,h):
    next = my_list[i]+my_list[i-1]
    my_list.append(next)



print(my_list)