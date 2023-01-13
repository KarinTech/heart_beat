import csv


def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    db = {}
    with open(filename) as students:
        reader = csv.reader(students)
        next(reader)

        for key, value in reader:
            db[key] = value
    return db


def main():
    students_db = read_dictionary('students.csv')
    print(students_db)
    id = input('Please enter an I-Number (xxxxxxxxx): ')
    id = id.replace('-', '')

    if len(id) < 9:
        return print('Invalid I-Number: too few digits')
    elif len(id) > 9:
        return print('Invalid I-Number: too many digits')
    elif not id.isdigit():
        return print('Invalid I-Number')
    else:
        if id in students_db:
            student = students_db[id]
            print(student)
        else:
            print('No such student')


if __name__ == "__main__":
    main()
