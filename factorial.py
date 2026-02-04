
def recursive_factorial(n):
    # Base condition
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)




number = int(input("Enter a non-negative integer: "))


if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
 
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i

    print("Factorial using iterative method is:", factorial)


# OUTPUT
Enter a non-negative integer: 14
Factorial using iterative method is: 87178291200

=== Code Execution Successful ===
