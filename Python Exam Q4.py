def duplicate_string_detector():
    user_strings = []
    duplicates = []


    while True:
        text = input("Enter a word: ")
        print("enter 'quit' to exit")
        if text == "quit":
            break

        if text in user_strings and text not in duplicates:
            duplicates.append(text)

        user_strings.append(text)

    if len(user_strings) != len(set(user_strings)):
        print("There were duplicate words")
        print(duplicates)
    else:
        print("There were no duplicate words")

duplicate_string_detector()