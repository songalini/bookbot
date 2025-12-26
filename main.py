from stats import get_word_count, get_char_count, build_char_report                 #import functions from stats.py
import sys                                                                          #import sys

def main():
    #main program function
    if len(sys.argv) <2:                                            #if len of sys.argv is <2, aka you're not using the program correctly  
        print("Usage: python3 main.py <path_to_book>")              #explain how to use it
        print("Example: 'python main.py books/frankenstein.txt'")   
        print("Exiting...")
        sys.exit(1)                                                 #exits the program with the error code 1

    path = sys.argv[1]                                              #path variable set to sys.argv[1], aka the term for the file location
    
    report = (                                                      #prints the report, calling functions from stats.py
        f"============ BOOKBOT ============\n"
        f"\n"
        f"Analyzing book found at {path}...\n"
        f"\n"
        f"----------- Word Count ----------\n"
        f"\n"
        f"Found {get_word_count(path)} total words\n"
        f"\n"
        f"--------- Character Count -------\n"
        f"\n"
        f"{build_char_report(path)}"
        f"\n"
        f"=================================\n"
    )

    print(report)

main()    