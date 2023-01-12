import random


def main():
    numbers = [3.4, 7.5]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)
    words = ["fantasy", "seed", "declaration", "highlight", "auditor"]
    append_random_words(words, 4)
    print(words)


def append_random_numbers(numbers_list, quantity=1):
    """Add to the list a quantity of random numbers.

    Parameters:
        numbers_list: list of numbers
        quantity: numbers quantity to be added to numbers list. Default value 1.
    """
    for _ in range(quantity):
        numbers_list.append(round(random.uniform(0, 10), 1))


def append_random_words(words_list, quantity=1):
    """Add quantity words to the words list.

    Parameters:
        words_list: list of words
        quantity: an integer. Default value 1.
    """
    random_words = ["define", "harbor", "line", "raw", "suffer",
                    "species", "discovery", "retreat", "modernize", "excess", ]
    for _ in range(quantity):
        words_list.append(random.choice(random_words))


if __name__ == "__main__":
    main()
