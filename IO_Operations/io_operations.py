'''1.Write a program to read the entire content from a txt file and display it to the user.'''



filename = "student.txt"

try:
    
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile Content:\n")
        print(content)
except FileNotFoundError:
    print("File 'student.txt' not found. Please make sure the file exists in the same folder.")
except Exception as e:
    print("An error occurred:", e)


'''2.Write a program to read first n lines from a txt file. Get n as user input.'''
filename = "student.txt"
try:
    n = int(input("Enter the number of lines to read: "))
    with open(filename, 'r') as file:
        print(f"\nFirst {n} line(s) from {filename}:\n")
        for i in range(n):
            line = file.readline()
            if not line:
                break  
            print(line.strip())

except FileNotFoundError:
    print(f"File '{filename}' not found. Please check the file name.")
except ValueError:
    print("Please enter a valid integer for number of lines.")
except Exception as e:
    print("An error occurred:", e)


'''3.Write a program to accept input from user and append it to a txt file'''


filename = "student.txt"
user_input = input("Enter the text you want to append to the file: ")
try:
    with open(filename, 'a') as file:
        file.write(user_input + '\n')  
    print(f"Text appended successfully to '{filename}'.")
except Exception as e:
    print("An error occurred:", e)

'''4.Write a program to read contents from a txt file line by line and store each line into a list.'''

try:
    with open("student.txt", 'r') as file:
      lines = [line.strip() for line in file]
    print("Lines stored in the list:")
    print(lines)
except FileNotFoundError:
    print("File 'student.txt' not found.")
except Exception as e:
    print("An error occurred:", e)


'''5.Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it'''

filename = "student.txt"

try:
    with open(filename, 'r') as file:
        content = file.read() 

        
        words = content.split()
        longest_word = max(words, key=len)
    print("The longest word in the file is:", longest_word)

except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print("An error occurred:", e)

'''6.Write a program to count the frequency of a user entered word in a txt file.'''

# File name
filename = "student.txt"

# Ask user for the word to count
word_to_count = input("Enter the word to count in the file: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()

        count = words.count(word_to_count)
        print(f"The word '{word_to_count}' appears {count} time(s) in the file.")

except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print("An error occurred:", e)       
        
        
        






