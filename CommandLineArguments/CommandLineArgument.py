#1.Write a program to accept two numbers as command line arguments and display their sum. 
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



#2.Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

welcome_message = input("Enter your welcome message: ")


print("File Name:", __file__)
print("Welcome Message:", welcome_message)

#3.Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


input_str = input("Enter 10 numbers separated by space: ")


try:
    numbers = list(map(int, input_str.strip().split()))
    
    if len(numbers) != 10:
        print("Please enter exactly 10 numbers.")
    else:
       
        prime_sum = sum(num for num in numbers if is_prime(num))
        print("Sum of prime numbers:", prime_sum)

except ValueError:
    print("Please enter valid integers only.")

