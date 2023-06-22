import random

#design constraints:
#at least 1 lowercase, 1 upper case and, 1 digits, 1 symbols
#could generate length - 3, and then test?
#separate the lists, run choice for each seperated list, and then choices to fill out the rest of the length?
#   That solution is way better, since you avoid writing the conditional code, but still...


def generate_password_string(length):
    char_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    '^', '$', '*', '.', '[', ']', '{', '}', '(', ')', '?', '"', '!', 
    '@', '#', '%', '&', '/', '\\', ',', '>', '<', "'", ':', ';', '|', 
    '_', '~', '`'
    ]
    if length < 8:
        raise ValueError ('Use a longer length for your password code')
    
    lower_list = [letter for letter in char_list if letter.islower()]
    upper_list = [letter for letter in char_list if letter.isupper()]
    digit_list = [letter for letter in char_list if letter.isdecimal()]
    symbol_list = [letter for letter in char_list if not letter.isalnum()]

    sub_lists = [lower_list, upper_list, digit_list, symbol_list]
    password = [random.choice(list) for list in sub_lists]
    
    choices_length = length - len(sub_lists)
    password += random.choices (char_list, k= choices_length)
    
    random.shuffle(password)
    password = ''.join(password)
    print(password)

length = 15
generate_password_string(length)