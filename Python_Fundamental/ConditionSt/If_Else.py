# Write a program to check if a given number is Positive, Negative or Zero.
num=int(input("enter the number: "))
if num <0:
    print(f"given number {num} is Negative")
elif num==0:
    print(f"given number {num} is zero")
else:
    print(f"given number {num} is postive")

# 2. Write a program to check if a given number is odd or even.
num=int(input("enter the number: "))
if num%2==0:
    print(f"given number {num} is even")
else:
    print(f"given number is {num} odd")

# 3.Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.

num1=int(input("enter the Positive number 1: "))
num2=int(input("enter the Positive number 2: "))
if num1>0 and num2>0:
    if num1%10==num2%10:
        print("True")
else:
    print("plese enter correct number")

# 4.Write a program to print numbers from 1 to 10 in a single row with one tab space.

for i in range(1,11):
    print(i, end='\t')

# 5.Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

for num in range(23,58):
    if num%2==0:
        print(num)

# 6.Write a program to check if a given number is prime or not.
num=int(input("enter the number: "))
if num<1:
    print("number is not a prime number")
else:
    for i in range(2,int(num**0.5)+1):
        if num%1==0:
            print(f"number {num} is not a prime")
            break
    else:
        print(f"number is  a prime")

# 7.Write a program to print prime numbers between 10 and 99.
for num in range(10, 100):  
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, int(num**0.5) + 1): 
            if num % i == 0:
                is_prime = False
                break
    if is_prime:
        print(num, end=' ')

# 8. Write a program to print the sum of all the digits of a given number.

num=int(input("enter the number: "))
sum_digit=0
for digit in str(num):
    sum_digit+=int(digit)
print(sum_digit)

# Q9. Write a program to reverse a given number and print.
num=int(input("enter the number: "))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(reverse)

# Q10. Write a program to find if the given number is palindrom or not.
num=int(input("enter the number: "))
orignal_num=num
reverse_num=0
while num>0:
    digit=num%10
    reverse_num=reverse_num*10+digit
    num=num//10
if orignal_num==reverse_num:
    print(orignal_num)
else:
    print("number is not a palindrow")

