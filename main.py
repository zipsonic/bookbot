def main():
    bookpath = "books/frankenstein.txt"
    numwords = countwords(openbook(bookpath))
    print(f"{numwords} found in {bookpath}")
    print(charfreq(openbook(bookpath)))

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
       