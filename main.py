
def get_text(path):                                                                                    # function to read text from file as a string
    with open(path) as f:
        return f.read()

def word_count(words):                                                                                 # function to count total words from string
    word_amount = words.split()                                                                        # split string into list of strings
    return len(word_amount)                                                                            # return the length of the list

def lowercase_words(words):                                                                            # function to convert all letters to lowercase for counting
    lowercase = words.lower()                                                                          # create new variable with all letters lowercase
    lowercase_words = []                                                                               # create empty list
    for i in range(len(lowercase)):                                                                    # iterate over the string of lowercase letters
        if lowercase[i].isalpha():                                                                     # if the letter is an alphabet character
            lowercase_words.append(lowercase[i])                                                       # append it to the new list (lowercase_words)
    return lowercase_words                                                                             # return our lowercase_words list

def character_dict_alpha(words):                                                                       # function to create a dictionary of how many times a letter exists
    character_dict = {}                                                                                # create empty dict
    character_list = lowercase_words(words)                                                            # create a list of lowercase characters using our lowercase_words func
    character_list.sort()                                                                              # sort our character list alphabetically
    for i in range(len(character_list)):                                                               # for each item, iterating over our character_list list  
        if character_list[i] in character_dict:                                                        # check if the item is in our dictionary
            character_dict[(character_list[i])] += 1                                                   #  if it is, increment count
        else:                                                                                          # if it isn't, 
            character_dict[(character_list[i])] = 1                                                    # add it and begin count at 1
    return character_dict                                                                              # return our alphabetised character dictionary
    
def character_dict_numerical(character_dictionary_alpha):                                              # function to sort our dictionary by highest value
    character_dict_num = {}                                                                            # create new dictionary
    for k, v in sorted(character_dictionary_alpha.items(), key=lambda item:item[1], reverse=True):     # for key and value in our alphabetic dictionary, sorted by the second item (the value), sorted highest-to-lowest
        character_dict_num[k] = v                                                                      # add them to the dictionary ^^in the order highest to lowest
    return character_dict_num                                                                          # return our newly sorted dictionary
    
    

def characters_total(words):                                                                           # function to count total characters
    character_list = list(lowercase_words(words))                                                      # variable that is the list of all lowercase characters
    character_total = len(character_list)                                                              # int variable that is the length of that list
    return character_total                                                                             # return the total character list

def main():
    book_path = "books/frankenstein.txt"                                                               # string to manage book path
    words = get_text(book_path)
    num_words = word_count(words)
    num_chars = characters_total(words)
    character_dictionary_alpha = character_dict_alpha(words)
    character_dict_num = character_dict_numerical(character_dictionary_alpha)
    print(f"--- Content Summary of {book_path} --- \n")                                                # print title 
    print(f"{num_words} words were found, with a total of {num_chars} letters \n")                       # print wordcount and character count
    for char, amount in character_dict_num.items():                                                    # check character and amount in our numerically-sorted dictionary
        print(f"Character '{char}' was found {amount} times!")                                         # print the character summary
    print(f"\n --- End of Content Summary ---")                                                          # print closing statement
    


    
main()
