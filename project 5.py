'''
In this project, the user can input a text paragraph or a file,
 and the program will count the number of words, sentences, and characters in the given input.
 It's a simple tool that can be useful for basic text analysis. Let's get started:'''

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = text.split('.')
    return len(sentences)

def count_characters(text):
    return len(text)

def word_count_tool():
    print("Word Count Tool")
    print("1. Count words")
    print("2. Count sentences")
    print("3. Count characters")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            print("Exiting the Word Count Tool.")
            break

        if choice not in ('1', '2', '3'):
            print("Invalid choice. Please try again.")
            continue

        if choice in ('1', '2', '3'):
            input_text = input("Enter the text or type 'file' to read from a file: ")

            if input_text.lower() == 'file':
                filename = input("Enter the file name (including extension): ")
                try:
                    with open(filename, 'r') as file:
                        input_text = file.read()
                except FileNotFoundError:
                    print("File not found. Please check the file name and try again.")
                    continue

            if choice == '1':
                word_count = count_words(input_text)
                print(f"Number of words: {word_count}")
            elif choice == '2':
                sentence_count = count_sentences(input_text)
                print(f"Number of sentences: {sentence_count}")
            elif choice == '3':
                char_count = count_characters(input_text)
                print(f"Number of characters: {char_count}")

if __name__ == "__main__":
    word_count_tool()









