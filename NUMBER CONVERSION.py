def convert_to_base(num, base):
    # Handle zero as a special case
    if num == 0:
        return "0"

    digits = []
    temp = num
    while temp > 0:
        digits.append(str(temp % base))
        temp //= base

    # Since digits are collected in reverse, reverse them before joining
    digits.reverse()
    return ''.join(digits)


# Main program
num = int(input("Enter a number: "))
base = int(input("Enter the base: "))

converted = convert_to_base(num, base)
print(f"The number {num} in base {base} is: {converted}")

#OUTPUT
Enter a number: 6
Enter the base: 4
The number 6 in base 4 is: 12

=== Code Execution Successful ===
