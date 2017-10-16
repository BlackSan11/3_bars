import json
import math
import sys

#выгружаем JSON из файла
def load_data_from_file(filepath):
    with open(filepath, "r", encoding='utf-8') as file_with_json:
        json_from_file = file_with_json.read()
        loaded_json = json.loads(json_from_file)
        return loaded_json

#ищем самый вместительный бар
def get_biggest_bar(json_data):
    all_bars = json_data['features']
    bar = max(all_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return bar

def get_smallest_bar(json_data):
    all_bars = json_data['features']
    bar = min(all_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return bar

def get_closest_bar(json_data, me_X_coordinate, me_Y_coordinate):
    all_bars = json_data['features']
    bar = min(all_bars, key=lambda x: math.sqrt(((float(me_X_coordinate) - x['geometry']['coordinates'][0])**2) + ((float(me_Y_coordinate) - x['geometry']['coordinates'][1])**2)))
    return bar['properties']['Attributes']['Name']

if __name__ == '__main__':
    datat = get_biggest_bar(load_data_from_file(sys.argv[1]))
    datatmin = get_smallest_bar(load_data_from_file(sys.argv[1]))
    print("Наиболей вместимостью славится \"{}\" - {} мест, находящийся по адресу: г. Москва, {}, телефон - +7 {}".format(datat['properties']['Attributes']['Name'],datat['properties']['Attributes']['SeatsCount'],datat['properties']['Attributes']['Address'],datat['properties']['Attributes']['PublicPhone'][0]['PublicPhone']))
    print(
        "Самой маленькой вместимостью славится \"{}\" - {} мест, находящийся по адресу: г. Москва, {}, телефон - +7 {}".format(
            datatmin['properties']['Attributes']['Name'], datatmin['properties']['Attributes']['SeatsCount'],
            datatmin['properties']['Attributes']['Address'],
            datatmin['properties']['Attributes']['PublicPhone'][0]['PublicPhone']))
    print("Рядом с Вами {}".format(get_closest_bar(load_data_from_file(sys.argv[1]), sys.argv[2], sys.argv[3])))