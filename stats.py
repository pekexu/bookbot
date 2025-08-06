def get_book_text(file_path):
    with open(file_path) as f:
        book = f.read()
    return book

def get_num_words(book):
    book_text = get_book_text(book)
    return len(book_text.split())

def count_the_letters(bookstring):
    letters = {}
    bookstring = bookstring.lower()

    for i in bookstring:
        if i in letters:
            letters[i] += 1
        else: 
            letters[i] = 1
    return letters

def get_sorted_list(path_to_file):
    
    def sort_on(items):
        return items["num"]
    
    list_dict = []
    old_dict = count_the_letters(get_book_text(path_to_file))
    
    for i in old_dict:
        j = old_dict[i]
        list_dict.append({"char": i, "num": j})
    
    list_dict.sort(reverse=True, key=sort_on)
    return(list_dict)
    


