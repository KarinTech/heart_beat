import csv


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dict = {}
    with open(filename) as products:
        reader = csv.reader(products)
        next(reader)
        for row in reader:
            dict[row[key_column_index]] = row
    return dict


def main():
    products_dict = read_dictionary('products.csv', 0)
    print(f'All Products\n{products_dict}')

    print('\nRequested Items')
    with open('request.csv') as request:
        requests = csv.reader(request)
        next(requests)
        for request in requests:
            product_name = products_dict[request[0]][1]
            quantity = request[1]
            product_price = products_dict[request[0]][2]
            print(f'{product_name}: {quantity} @ {product_price}')


if __name__ == '__main__':
    main()
