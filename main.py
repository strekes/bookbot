import sys
from stats import word_count
from stats import repeats
from stats import sort_dict

def get_book_text(book):
    with open (book) as text:
        return text.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        raise sys.exit(1)
    book = sys.argv[1]
    get_book_text(book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book + "...")
    print("----------- Word Count ----------")
    print("Found " + str(word_count(get_book_text(book))) + " total words")
    print("--------- Character Count -------")
    for x in sort_dict(repeats(get_book_text(book))):
        print(x["char"] + ": " + str(x["num"]))
    print("============= END ===============")




main()