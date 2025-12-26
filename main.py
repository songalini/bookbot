from stats import get_word_count, get_char_count, build_char_report
import sys

def main():
    if len(sys.argv) <2:
        print("How to use: 'python main.py <path-to-book>'")
        print("Example: 'python main.py books/frankenstein.txt'")
        print("Exiting...")
        sys.exit(1)
    path = sys.argv[1]
    
    report = (
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {path}...\n"
        f"\n"
        f"----------- Word Count ----------\n"
        f"Found {get_word_count(path)} total words\n"
        f"\n"
        f"--------- Character Count -------\n"
        f"{build_char_report(path)}"
        f"\n"
        f"=================================\n"
    )
    print(report)
    print(sys.argv)

main()    