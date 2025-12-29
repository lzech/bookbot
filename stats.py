def get_number_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

def count_characters(text):
    num_characters = {}
    text = text.lower()
    for word in text.split():
        for character in word:
           num_characters.update({character: num_characters.get(character, 0) + 1})
    return num_characters

def sort_dict(dict):
    sorted_dict = sorted(dict.items(), key=lambda item:item[1], reverse=True)
    return sorted_dict


