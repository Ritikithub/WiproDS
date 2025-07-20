'''1.Write a function to return the sum of all numbers in a list.'''

# def sum_of_list(num):
#     return sum(num)

# list_1=[1,2,3,4,5]
# sum=sum_of_list(list_1)
# print(sum)

'''2.Write a function to return the reverse of a string.
Sample String: "1234abcd"

Expected Output:"dcba4321"'''
# def reverse_of_str(s):
#     return s[::-1]

# stri="1234abcd"
# reverse_str=reverse_of_str(stri)
# print(reverse_str)

'''3.Write a function to calculate and return the factorial of a number (a non-negative integer'''
# def factorial(n):
#     if n < 0:
#         return "Invalid input."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print("Factorial of given of number is:", factorial(15))

'''4.Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.'''
# def count_case_letters(text):
#     upper_count = 0
#     lower_count = 0

#     for char in text:
#         if char.isupper():
#             upper_count +=1
#         elif char.islower():
#             lower_count +=1
#             print("Uppercase letters:", upper_count)
#             print("Lowercase letters:", lower_count)
# Str_1= "Hello im ritik singh and learn python AND dsTA scIeNce"
# count_case_letters(Str_1)

'''5.Write a function to print the even numbers from a given list. List is passed to the function as an argument. 
Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
 Expected Result [2,4,6,8]'''

# def even_number_of_list(number):
#     even_list=[]
#     for num in number:
#         if num%2==0:
#             even_list.append(num)
#     return even_list


# list_1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(even_number_of_list(list_1))

'''6.Write a function that takes a number as a parameter and checks whether the number is prime or not'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(1,int(n ** 0.5) +1):
        if n % i == 0:
            return False 
    return True

num = 5
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")