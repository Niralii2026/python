largest_odd = None

print("Enter 10 numbers:")

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    
    if num % 2 != 0:  # Check if number is odd
        if largest_odd is None or num > largest_odd:
            largest_odd = num

# Output result
if largest_odd is not None:
    print("Largest odd number is:", largest_odd)
else:
    print("No odd number was entered.")