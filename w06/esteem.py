# Colors
green_color = '\033[0;32m'
yellow_color = '\033[0;33m'
red_color = '\033[0;31m'
end_color = '\033[0m'

print(
    f'\nThis program is an implementation of the Rosenberg\nSelf-Esteem Scale. This program will show you ten\nstatements that you could possibly apply to yourself.\nPlease rate how much you agree with each of the\nstatements by responding with one of these four letters:\n\n{green_color}D{end_color} means you strongly disagree with the statement.\n{green_color}d{end_color} means you disagree with the statement.\n{green_color}a{end_color} means you agree with the statement.\n{green_color}A{end_color} means you strongly agree with the statement.\n')

statements = ["I feel that I am a person of worth, at least on an equal plane with others.",
              "I feel that I have a number of good qualities.",
              "All in all, I am inclined to feel that I am a failure.",
              "I am able to do things as well as most other people.", "I feel I do not have much to be proud of.",
              "I take a positive attitude toward myself.", "On the whole, I am satisfied with myself.",
              "I wish I could have more respect for myself.", "I certainly feel useless at times.",
              "At times I think I am no good at all."]


def negative_scores(choice):
    """
    Determine which value the user choice will have

    Parameter:
        choice: users choice
    Return: value from the users choice
    """
    score = 0
    if choice == 'D':
        score = 3
    elif choice == 'd':
        score = 2
    elif choice == 'a':
        score = 1
    elif choice == 'A':
        score = 0
    return score


def positive_scores(choice):
    """
    Determine which value the user choice will have

    Parameter:
        choice: users choice
    Return: value from the users choice
    """
    score = 0
    if choice == 'D':
        score = 0
    elif choice == 'd':
        score = 1
    elif choice == 'a':
        score = 2
    elif choice == 'A':
        score = 3
    return score


def scores(statement, choice):
    """
    Determine which scores will be used.

    Parameters:
        statement: Number of statement.
        choice: Users choice.
    Return: a function that calculate the score from the user choice.
    """
    if statement in [1, 2, 4, 6, 7]:
        return positive_scores(choice)
    elif statement in [3, 5, 8, 9, 10]:
        return negative_scores(choice)


def start():
    """The program starts here.
    """
    score = 0
    for i in range(len(statements)):
        print(f'{yellow_color}{i+1}.{end_color} {statements[i]}')
        choice = input(
            f'Enter {green_color}D{end_color}, {green_color}d{end_color}, {green_color}a{end_color}, or {green_color}A{end_color}:\n\t{yellow_color}-->>{end_color}  ')
        print()
        score += scores(i + 1, choice)
    print_result(score)


def print_result(score):
    """Print the total score.

    Parameter:
        score: Total score.
    """
    print(
        f'{green_color}¬{end_color} Your score is {green_color}{score}{end_color}.\n\n{red_color}[!]{end_color} A score below 15 may indicate problematic low self-esteem.\n')


def main():
    start()


if __name__ == '__main__':
    main()
