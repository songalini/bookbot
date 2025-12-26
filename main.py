from stats import get_word_count, get_char_count, build_char_report
import sys

def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        # print("Example: 'python main.py books/frankenstein.txt'")
        # print("Exiting...")
        sys.exit(1)
    path = sys.argv[1]
    
    report = (
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