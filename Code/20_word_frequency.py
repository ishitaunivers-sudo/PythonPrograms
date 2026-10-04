import re


def word_frequency(sentence):
    words = re.findall(r"\b\w+\b", sentence.lower())
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


if __name__ == "__main__":
    print(word_frequency("Python is easy and Python is powerful"))