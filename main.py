def main():
    bookpath = "books/frankenstein.txt"
    book_string = openbook(bookpath)
    report = charfreq(book_string)
    numwords = countwords(book_string)
    print(f"Begin report of {bookpath}")
    print(f"{numwords} words found in book")
    for a in range (97,123):
        print(f"{chr(a)} was found {report[chr(a)]} times")
    print("---- END REPORT")

def openbook(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
    return file_contents

def countwords(file_contents):
    return len(file_contents.split())

def charfreq(file_contents):
    char_dict = {}
    for character in file_contents.lower():
        if character in char_dict:
            char_dict[character] = char_dict[character] + 1
        else:
            char_dict[character] = 1
    return char_dict

main()
       