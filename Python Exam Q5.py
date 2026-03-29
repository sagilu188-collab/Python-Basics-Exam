import string

def find_most_common():
    user_text = input("Enter your text here: ")

    for char in string.punctuation:
        user_text = user_text.replace(char, "")

    words = user_text.lower().split()
    if not words:
        print("No words found")
        return
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    best_word = max(word_counts, key=word_counts.get)
    count = word_counts[best_word]

    print(f"\n{best_word}")
    print(f"{count} times")

find_most_common()