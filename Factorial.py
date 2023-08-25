# Problem 5b: Factorial.py Write a Python program that calculates the factorial of a given non-negative integer.
import sys
sys.set_int_max_str_digits(10000)
total=1
i =int (input("what is the integer you want   "))
for g  in range(1,i+1):
    print(total,g)

    total=total*g


print(total)
print("--------------------------------------------------------------------")