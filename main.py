import sys
from stats import get_num_words , get_char_frequency, sort_char_frequency

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]     
    book_text = get_book_text(path_to_file)
    
    num_words = get_num_words(book_text)
    char_frequency = get_char_frequency(book_text)
    char_frequency = sort_char_frequency(char_frequency) 

    print(f"{' BOOKBOT ':=^33}")
    print(f"Analyzing book found at {path_to_file}...")

    print(f"{' Word Count ':-^33}")
    print(f"Found {num_words} total words")
    
    print(f"{' Character Count ':-^33}")
    print("\n".join([f"{k}: {item[k]}" for item in char_frequency for k in item]))

main()
