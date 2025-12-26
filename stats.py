def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def get_word_count(path):
    text = get_book_text(path)
    words = text.split()
    wordcount = len(words)
    return wordcount

def get_char_count(path):
    text = get_book_text(path).lower()
    char_counter = {}
    for char in text:
        if char.isalpha():
            if char in char_counter:
                char_counter[char] += 1
            else: 
                char_counter[char] = 1
    return char_counter 
    
def sort_on(item):
    return item["num"]

def sort_char_count(path):
    char_count = get_char_count(path)
    char_list = []
    for char, count in char_count.items():
        char_dict = {
            "char": char,
            "num": count
        }
        char_list.append(char_dict)
    char_list.sort(key=sort_on, reverse = True)
    return char_list

def build_char_report(path):
    sorted_chars = sort_char_count(path)
    lines = ""
    for item in sorted_chars:
        if item["char"].isalpha():
            lines += f"{item['char']}: {item['num']}\n"
    return lines