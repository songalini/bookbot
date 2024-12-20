def main():
    book_path = "books/frankenstein.txt" 
    words = get_text(book_path)
    num_words = word_count(words)
    num_chars = characters_total(words)
    character_dictionary_alpha = character_dict_alpha(words)
    character_dict_num = character_dict_numerical(character_dictionary_alpha)
    print(f"--- Content Summary of {book_path} --- \n")
    print(f"{num_words} words were found, with a total of {num_chars} letters ")
    for char, amount in character_dict_num.items():
        print(f"Character '{char}' was found {amount} times!")
    print(f" --- End of Content Summary ---")
    
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

def character_dict_alpha(words):
    character_dict = {}
    character_list = list(lowercase_words(words))
    character_list.sort()
    for i in range(len(character_list))[1::]:
        if character_list[i] in character_dict:
            character_dict[(character_list[i])] += 1
        else:
            character_dict[(character_list[i])] = 1
    return character_dict
    
def character_dict_numerical(character_dictionary_alpha):
    character_dict_num = {}
    for k, v in sorted(character_dictionary_alpha.items(), key=lambda item:item[1], reverse=True):
        character_dict_num[k] = v
    return character_dict_num
    
    

def characters_total(words):
    character_list = list(lowercase_words(words))
    character_total = len(character_list)
    return character_total

main()
