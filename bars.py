import json


def load_data(filepath):
    with open(filepath, "r") as file_with_json:
        json_from_file = file_with_json.read()
        loaded_json = json.loads(json_from_file)
        return loaded_json


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    print(load_data('base.json'))
d