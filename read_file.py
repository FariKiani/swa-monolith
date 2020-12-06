import csv, sys


def read_file(filename, mapping):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        try:
            return [mapping(row) for row in reader]
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
