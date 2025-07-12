def get_num_words(text):
    words = text.split()
    return(len(words))

def sort_on(items):
    sorted_items = sorted(items.items(), key=lambda item: item[1], reverse=True)
    return sorted_items

def word_stats(text):
    words = text.split()
    word_dict = {}
    for word in words:
        for letter in word:
            lower_letter = letter.lower()
            if lower_letter not in word_dict:
                word_dict[lower_letter] = 0
            word_dict[lower_letter] += 1

    return word_dict
