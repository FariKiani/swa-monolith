from read_file import read_file


def get_service_list():
    filename = 'input/service_list.csv'
    return read_file(filename, lambda row:row[0])
