def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #return (f"This book had {number_of_words(text)} words.")
    #return (f"This book's letter breakdown is as follows: {number_of_letters(text)}")
    return (f"{full_report(text)}")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_letters(text):
    num_of_letters = {}
    for letter in text:
        letter_lowered = letter.lower()
        if letter_lowered in num_of_letters:
            num_of_letters[letter_lowered] += 1
        else:
            num_of_letters[letter_lowered] = 1
    return num_of_letters
        
def full_report(text):
    unsorted = number_of_letters(text)
    sorted_char = []
    for unst in unsorted:
        if unst.isalpha():
            sorted_char.append(unst)
            sorted_char.sort()
    print("- - - Begin Report of 'Frankenstein' - - -")
    print(f"{number_of_words(text)} words are in this document.")
    print("")
    for char in sorted_char:
        print(f"The letter '{char}' was found {unsorted[char]} times.")
    print("")
    return print("- - - End Report - - -")

        
    
main()