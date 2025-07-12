from stats import get_num_words
from stats import word_stats
from stats import sort_on
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    raise Exception()

def main():

    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]
    try:
        text = get_book_text(book)
    except Exception as e:
        print(e)
        sys.exit(1)
        
    word_count = get_num_words(text)
    word_dict = word_stats(text)
    sorted_word_dict = sort_on(word_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for letter in sorted_word_dict:
        if(letter[0].isalpha()):
            print(f"{letter[0]}: {letter[1]}")

    print("============= END ===============")


main()
    

