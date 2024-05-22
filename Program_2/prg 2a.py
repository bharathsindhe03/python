# Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program which accepts a value for N (where N >0) as input and pass this value to the function. Display suitable error message if the condition for input value is not followed. 
def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (Fibonacci(n-1)+Fibonacci(n-2))


num = int(input("Enter the number\n"))
if num > 0:
    res = Fibonacci(num)
    print("Fibonacci of ", num, "is", res)
else:
    print("Error in the input")
