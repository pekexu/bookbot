import sys
from stats import get_num_words
from stats import get_sorted_list


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    bookname = sys.argv[1]
    sorted_list = get_sorted_list(bookname)
    #count_the_letters(get_book_text("books/frankenstein.txt"))
    
    #print(sorted_list)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", bookname)
    print("----------- Word Count ----------")
    print("Found", get_num_words(bookname), "total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
main()
    
    