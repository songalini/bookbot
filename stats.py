def get_book_text(path):
    # function to get the book text
    with open(path) as f:       # using open(path) to get the text
        contents = f.read()     # uses .read() to pull the text from the path/file and set to a string
    return contents             # returns the string

def get_word_count(path):
    #function to count words and return the count
    text = get_book_text(path) #gets text from path using get_book_text
    words = text.split()       #splits text into a list of words 
    wordcount = len(words)     #counts the list of words 
    return wordcount           #returns the count

def get_char_count(path):
    #function to count individual characters
    text = get_book_text(path).lower()          #gets text from path using get_book_text, ',lower()' forces all text to be lowercase
    char_counter = {}                           #starts empty dictionary to count the words
    for char in text:                           #for each character in the text
        if char.isalpha():                      #if it is an alphabetic character
            if char in char_counter:            #if it is in the char_counter dictionary
                char_counter[char] += 1         #increment by 1
            else:                               #if it isn't in the dictionary
                char_counter[char] = 1          #set count to 1
    return char_counter                         #return dictionary
    
def sort_on(item):                              
    #sort_on helper function
    return item["num"]                          #return "item["num"]"

def sort_char_count(path):
    #function to sorth the char_counter dictionary by frequency
    char_count = get_char_count(path)           #uses get_char_count to get the dictionary of characters
    char_list = []                              #starts a new list
    for char, count in char_count.items():      #for each char and count in the dictionary
        char_dict = {                          
            "char": char,                       #key = char
            "num": count                        #value = num
        }
        char_list.append(char_dict)             #append the character:amount pair as it's own dictionary to the char_list list
    char_list.sort(key=sort_on, reverse = True) #sorts the list by "num" (frequency) of the characters, using the sort_on helper function as the key
    return char_list                            #returns the list

def build_char_report(path):
    #function to print the character list for the report
    sorted_chars = sort_char_count(path)                    #gets the sorted list of character:frequency dictionaries from sort_char_count
    lines = ""                                              #starts a new empty string
    for item in sorted_chars:                               #for each dictionary in sorted_chars
        if item["char"].isalpha():                          #if the item is alphabetical (Redundant, we already did this in get_char_count)
            lines += f"{item['char']}: {item['num']}\n"     #add the character:frequency pair to the string, followed by a new line (\n)
    return lines                                            #return lines string