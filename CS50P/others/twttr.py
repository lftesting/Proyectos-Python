def main():
    print(shorten("word"))


def shorten(word):
    word = (input("Input: "))
    remove = "aAeEiIoOuU"
    for i in remove:
        word = word.replace(i,"")
    return word


if __name__ == "__main__":
    main()
