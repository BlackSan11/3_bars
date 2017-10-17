import json
import math
import sys


def load_data_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file_with_json:
        json_from_file = json.load(file_with_json)
        return json_from_file


def get_biggest_bar(json_data):
    all_bars = json_data['features']
    bar = max(all_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return bar['properties']['Attributes']


def get_smallest_bar(json_data):
    all_bars = json_data['features']
    bar = min(all_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return bar['properties']['Attributes']


def get_closest_bar(json_data, me_X_coordinate, me_Y_coordinate):
    all_bars = json_data['features']
    bar = min(all_bars, key=lambda x: math.sqrt(((float(me_X_coordinate) - x['geometry']['coordinates'][0])**2) + ((float(me_Y_coordinate) - x['geometry']['coordinates'][1])**2)))
    return bar['properties']['Attributes']


if __name__ == '__main__':
    biggest_bar = get_biggest_bar(load_data_from_file(sys.argv[1]))
    smallest_bar = get_smallest_bar(load_data_from_file(sys.argv[1]))
    closest_bar = get_closest_bar(load_data_from_file(sys.argv[1]), sys.argv[3], sys.argv[2])
    print(
        "Хотите много места? Тогда вам в \"{}\" в нем {} мест, он находится по адресу: г. Москва, {}, телефон - +7 {}".format(
            biggest_bar['Name'],
            biggest_bar['SeatsCount'],
            biggest_bar['Address'],
            biggest_bar['PublicPhone'][0]['PublicPhone']))
    print(
        "Самым маленьким заведением является \"{}\" - {} мест, находящийся по адресу: г. Москва, {}, телефон - +7 {}".format(
            smallest_bar['Name'],
            smallest_bar['SeatsCount'],
            smallest_bar['Address'],
            smallest_bar['PublicPhone'][0]['PublicPhone']))
    print(
        "Рядом с Вами находиться {}, в нем - {} мест, он находиться по адресу: г. Москва, {}, телефон - +7 {}".format(
            closest_bar['Name'],
            closest_bar['SeatsCount'],
            closest_bar['Address'],
            closest_bar['PublicPhone'][0]['PublicPhone']))
