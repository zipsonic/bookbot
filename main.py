def main():
    bookpath = "books/frankenstein.txt"
    numwords = countwords(openbook(bookpath))
    print(f"{numwords} found in {bookpath}")


def openbook(bookpath):
    with open(bookpath) as f:
        file_contents = f.read()
    return file_contents

def countwords(file_contents):
    return len(file_contents.split())

main()
       