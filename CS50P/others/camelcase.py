
def change_case(camel):
    snake = ""
    for i in camel:
        if i.isupper():
            if snake:
                snake += "_"
            snake += i.lower()
           
        else:
            snake += i
    return snake

def main ():
    camel_case = input("camelCase: ")
    snake_case = change_case(camel_case)
    print("snake_case:", snake_case)

if __name__ == "__main__":
    main()