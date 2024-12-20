def main():
    book_path = "books/frankenstein.txt" 
    words = get_text(book_path)
    num_words = word_count(words)
    lower = lowercase_words(words)
    num_chars = characters_total(words)
    character_dictionary = character_list(words)
    print(f"--- Content Summary of {book_path} ---" )
    print(f"{num_words} words were found, with a total of {num_chars} letters ")
    for i in character_dictionary:
        print(f"Character '{i}' was found {character_dictionary[i]} times!")

def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(words):
    word_amount = words.split()
    return len(word_amount)

def lowercase_words(words):
    lowercase = words.lower()
    lowercase_words = []
    for i in range(len(lowercase)):
        if lowercase[i].isalpha():
            lowercase_words.append(lowercase[i])
    return lowercase_words 

def character_list(words):
    character_dict = {
    }
    character_list = list(lowercase_words(words))
    character_list.sort()
    for i in range(len(character_list))[1::]:
        if character_list[i] in character_dict:
            character_dict[(character_list[i])] += 1
        else:
            character_dict[(character_list[i])] = 1
    return character_dict

def characters_total(words):
    character_list = list(lowercase_words(words))
    character_total = len(character_list)
    return character_total

main()
