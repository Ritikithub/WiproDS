'''1.Through command line arguments three strings separated by space are given to you. Each string is a series of numbers separated by hyphen(-). You like all the numbers in string 1 and dislike all the numbers in string 2.

Third string contains the numbers given to you. Your initial happiness is 0.

When you encounter a number which is present in string 1, add 1 to your happiness, if it is present in string 2, add -1 to your happiness. Otherwise, your happiness does not change. Outpüt your final happiness at the end.
'''

like_str = input("Enter liked numbers (hyphen-separated): ")
dislike_str = input("Enter disliked numbers (hyphen-separated): ")
given_str = input("Enter given numbers (hyphen-separated): ")


like_set = set(like_str.strip().split('-'))
dislike_set = set(dislike_str.strip().split('-'))
given_numbers = given_str.strip().split('-')


happiness = 0


for num in given_numbers:
    if num in like_set:
        happiness += 1
    elif num in dislike_set:
        happiness -= 1


print(happiness)
