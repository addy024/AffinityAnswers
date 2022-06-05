# Python library to check for profanity in strings.
from better_profanity import profanity
# Csv file reader
import csv
    
def racialProfanityChecker(racial_slurs_file, tweets_file, toCsv):
    """ Checks for racial profanity slurs in strings and print results to the console.
    
    degree of racial profanity:
        0: Not racially profanity
        1: racially profanity 
    
    Args:
        racial_slurs_file: racial slurs file location
        tweets_file: tweets file location
        toCsv: takes boolean value whether to save result to file or not
    
    Returns: None
    """
    # Passing our racial slurs file
    profanity.load_censor_words_from_file(racial_slurs_file)
    # Reading tweets file
    with open(tweets_file) as file:
        csv_file = csv.reader(file, delimiter=",")
        # Following line return list
        for line in csv_file:
            # [0] contains user, [1] contains tweet, and passing tweet for racial profanity checking
            content = []
            content.append(line[0])
            content.append(line[1])  
            content.append(int(profanity.contains_profanity(line[1])))
            if toCsv:
                to_csv(content)
            else:
                print(content)


def to_csv(content):
    """ Takes content and write to csv file.

    Args:
        content: Content to write in file

    Return: None
    
    """
    with open("result.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(content)
