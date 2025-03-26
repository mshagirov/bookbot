"""
Functions for analysing text
"""

def get_num_words(text_str):
    return len(text_str.split())

def get_char_frequency(text_str):
    char_frequency = {}

    for c in text_str.lower():
        if c in char_frequency:
            char_frequency[c] += 1
        else:
            char_frequency[c] = 1

    return char_frequency

def sort_char_frequency(char_frequency):
    chars_list = [ { item[0] : item[1] } for item in char_frequency.items() if item[0].isalpha()]

    return sorted(chars_list, key= lambda d: list(d.values())[0], reverse=True)

