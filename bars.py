import json
import math
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='Get biggest, smallest and closest bars of Moscow')
    parser.add_argument("-c", nargs=2, type=float,
                        help="Plese input your coordinate")
    parser.add_argument("path", help="Plese input your path to json file")
    return parser


def load_data_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file_with_json:
        json_from_file = json.load(file_with_json)
        return json_from_file['features']


def get_biggest_bar(all_bars):
    bar = max(all_bars,
              key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return bar['properties']['Attributes']


def get_smallest_bar(all_bars):
    bar = min(all_bars,
              key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return bar['properties']['Attributes']


def get_closest_bar(all_bars, my_longitude, my_latitude):
    bar = min(all_bars,
              key=lambda x: math.sqrt(((my_longitude -
                                        x['geometry']['coordinates'][0])**2) +
                                      ((my_latitude -
                                        x['geometry']['coordinates'][1])**2)))
    return bar['properties']['Attributes']


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    json_from_file = load_data_from_file(args.path)
    biggest_bar = get_biggest_bar(json_from_file)
    smallest_bar = get_smallest_bar(json_from_file)
    closest_bar = get_closest_bar(json_from_file, args.c[0], args.c[0])
    print(
        "Хотите много места? Тогда вам в \"{}\" в нем {} мест, "
        "он находится по адресу: г. Москва, {}, телефон - +7 {}".format(
            biggest_bar['Name'],
            biggest_bar['SeatsCount'],
            biggest_bar['Address'],
            biggest_bar['PublicPhone'][0]['PublicPhone']))
    print(
        "Самым маленьким заведением является \"{}\" - {} мест,"
        " находящийся по адресу: г. Москва, {}, телефон - +7 {}".format(
            smallest_bar['Name'],
            smallest_bar['SeatsCount'],
            smallest_bar['Address'],
            smallest_bar['PublicPhone'][0]['PublicPhone']))
    print(
        "Рядом с Вами находится {}, в нем - {} мест,"
        " он находиться по адресу: г. Москва, {}, телефон - +7 {}".format(
            closest_bar['Name'],
            closest_bar['SeatsCount'],
            closest_bar['Address'],
            closest_bar['PublicPhone'][0]['PublicPhone']))
