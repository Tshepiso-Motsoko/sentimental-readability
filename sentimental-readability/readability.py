def main():
    # Get text from user
    text = input("Text: ")

    # Count letters, words, and sentences
    letters = sum(c.isalpha() for c in text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')

    # Calculate average number of letters and sentences per 100 words
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Calculate and round index
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # Print grade level
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

if __name__ == "__main__":
    main()
