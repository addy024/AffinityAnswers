from getopt import getopt   # For Error handling and exception
import sys
from ProfanityChecker import racialProfanityChecker

if __name__ == "__main__":
    
    try: 
        #
        if len(sys.argv) != 3:
            print("usage: main.py <racial_slurs_file> <tweets_csv_file>")
        else:        
            racial_slurs_file = sys.argv[1]     # racial slurs file name
            tweets_file = sys.argv[2]   # tweets file name
            racialProfanityChecker(racial_slurs_file=racial_slurs_file, tweets_file=tweets_file, toCsv=True)
    
    except getopt.GetoptError:
        print("usage: main.py <racial_slurs_file> <tweets_csv_file>")
        sys.exit(2)