import string

def count_word_occurrences(file_name):
    word_counts = {}

    with open(file_name, 'r') as file:
        for line in file:
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            words = line.split()

            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts

def display_word_counts(word_counts):
    sorted_words = sorted(word_counts.keys())

    for word in sorted_words:
        print(f"{word}: {word_counts[word]}")

file_name = 'file.txt'
word_counts = count_word_occurrences(file_name)
display_word_counts(word_counts)
