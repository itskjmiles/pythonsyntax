# Task 1

number1 = 10
number2 = 20

print("Initial value of number1:", number1)
print("Initial value of number2:", number2)

temp = number1
number1 = number2
number2 = temp

print("\nAfter swapping:")
print("Value of number1:", number1)
print("Value of number2:", number2)

if number1 == 20 and number2 == 10:
    print("\nThe values have been successfully swapped.")
else:
    print("\nError: The values have not been swapped correctly.")
