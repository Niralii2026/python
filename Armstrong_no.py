# Input from user
num = int(input("Enter a number: "))

# Store original number
temp = num
sum = 0

# Count number of digits
n = len(str(num))

# Calculate sum of digits raised to power n
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

# Check Armstrong condition
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")