# 1.Write a program to count the number of upper case lower case letters in string.
# s=input("enter string: ")
# upper_case=0
# lower_case=0
# for char in s:
#     if char.isupper():
#         upper_case+=1
#     else:
#         (char.islower())
#         lower_case+=1
# print(upper_case)
# print(lower_case)

# 2.Write a program that will check whether a given String is Palindrome or not.
# s=input("enter string: ")
# s=s.lower()
# reverse_s=s[::-1]
# if s==reverse_s:
#     print(f"string is palindron {s}")
# else:
#     print(f"string is not a palindorm {s}")

# 3.Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2. If input is "Wipro" then output should be "Wiwiwiwiwi"
# s=input("enter string: ")
# two_element=s[:2]
# new_s=two_element*len(s)
# print(new_s)

# 4.Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xhix", then output is "Hi".
# s=input("enter string: ")
# if s[0]=='x':
#     s=s[1:]
# if s[-1]=='x':
#     s=s[:-1]
# print(s)

# 5.Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between e and the length of the string inclusive. For example if the inputs are "Wipro" and 3, then the output should be "propropro".
s=input("enter string: ")
num=int(input("enter number: "))
s_new=s[-num:]*len(s)
print(s_new)
