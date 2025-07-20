'''1.Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with our python code'''

from collections import Counter
filename = "samplie.txt"
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    line_count = len(lines)
    
    if line_count == 0:
        print("File is empty. No secret message found.")
    else:
        if line_count > 12:
            hour = line_count % 12
            if hour == 0:
                hour = 12
            period = "PM"
        else:
            hour = line_count
            period = "AM"

        meeting_time = f"{hour} {period}"
        content = ' '.join(lines)
        words = content.split()
        words = [word.strip('.,!?').lower() for word in words]
        word_counts = Counter(words)
        most_common_word, _ = word_counts.most_common(1)[0]

        meeting_place = f"{most_common_word.capitalize()} Street"

        print("Secret Message Unlocked!")
        print(f" Meeting Time: {meeting_time}")
        print(f" Meeting Place: {meeting_place}")

except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print("An error occurred:", e)


        
       

        
        

       
        

       
       

       
        