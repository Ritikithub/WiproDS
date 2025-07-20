import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script_name.py num1 num2")
else:
    try:
        # Convert arguments to integers
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

        # Calculate and print the sum
        total = num1 + num2
        print("Sum:", total)
    except ValueError:
        print("Please enter valid integers.")