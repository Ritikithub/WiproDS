'''1.Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and his or her interesting fact to the screen. Next, change a fact about one of the people. Also add an additional person and corresponding fact. Display the new list of people and facts. Run the program multiple times and notice if the order changes.

Jeff: Is afraid of Dogs.
David: Plays the piano.
Jason: Can fly an airplane.
Jeff: Is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance.'''

# people_facts = {
#     "Jeff": "Is afraid of Dogs.",
#     "David": "Plays the piano.",
#     "Jason": "Can fly an airplane."
# }
# print("Original Facts:")
# for person, fact in people_facts.items():
#     print(f"{person}: {fact}")

# print()  
# people_facts["Jeff"] = "Is afraid of heights."
# people_facts["Jill"] = "Can hula dance."

# print("Updated Facts:")
# for person, fact in people_facts.items():
#     print(f"{person}: {fact}")


'''2.Given the participant's score sheet for your University Sports Day, you are required to find the runner-up score. You have scores. Store them in a list and find the score of the runner-up.
Sample input: [2, 3, 6, 6, 5]
Sample output: 5
Explanation: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second Г Hango we print 5 as the runner-up score.'''

# score=[2,3,6,6,5]
# set_1=list(set(score))
# set_1.remove(max(set_1))


# runner_up = max(set_1)

# print(f"runner_up: {runner_up}")

'''3.You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry. The marks can be floating values. You are required to save the record in a dictionary data type.
Student's name is the key. Marks stored in a list is the value. The user enters a student's name. Output the average percentage marks obtained by that student.

Formula: (sum of marks)/(no of subjects)

Sample input: "Krishna": (67, 68, 69]

"Arjun" : [70, 98, 631,

"Malika": 152, 56, 6011

Sample output:

Enter a name: Malika

Average percentage mark: 56

Explanation:

Marks for Malika are [52, 56, 60] whose average is (52+56+60)/356'''

# records={ "Krishna": [67, 68, 69],"Arjun" : [70, 98, 63],"Malika": [52, 56, 60]}
# name=input("enter the name of student: ")
# if name in records:
#     marks=records[name]
#     Average=sum(marks)/len(marks)
#     print(f"Average percentage mark: {int(Average)}")
# else:
#     print("student not found")

'''4.Given a string of n words, help Alex to find out how many times his name appears in the string.

Constraint: 1 <= n <= 200

Sample input: Hi Alex WelcomeAlex Bye Alex.

Sample output: 3

Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex Bye Alex.'''

text="Hi Alex WelcomeAlex Bye Alex."
count=text.count("Alex")
print(count)