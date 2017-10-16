import json
import math

#выгружаем JSON из файла
def load_data_from_file(filepath):
    with open(filepath, "r", encoding='utf-8') as file_with_json:
        json_from_file = file_with_json.read()
        loaded_json = json.loads(json_from_file)
        return loaded_json

#ищем самый вместительный бар
def get_biggest_bar(json_data):
    all_bars = json_data['features']
    biggest_bars = []
    bar = max(all_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return bar

def get_smallest_bar(json_data):
    all_bars = json_data['features']
    biggest_bars = []
    bar = min(all_bars, key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return bar

if __name__ == '__main__':
    datat = get_biggest_bar(load_data_from_file('base.txt'))
    datatmin = get_smallest_bar(load_data_from_file('base.txt'))
    print("Наиболей вместимостью славится \"{}\" - {} мест, находящийся по адресу: г. Москва, {}, телефон - +7 {}".format(datat['properties']['Attributes']['Name'],datat['properties']['Attributes']['SeatsCount'],datat['properties']['Attributes']['Address'],datat['properties']['Attributes']['PublicPhone'][0]['PublicPhone']))
    print(
        "Самой маленькой вместимостью славится \"{}\" - {} мест, находящийся по адресу: г. Москва, {}, телефон - +7 {}".format(
            datatmin['properties']['Attributes']['Name'], datatmin['properties']['Attributes']['SeatsCount'],
            datatmin['properties']['Attributes']['Address'],
            datatmin['properties']['Attributes']['PublicPhone'][0]['PublicPhone']))
    print(datat['geometry']['coordinates'][0], datat['geometry']['coordinates'][0])
    tempX = 37.582437591897381
    tempY = 55.843665951674964
    distance1 = ((tempX - datat['geometry']['coordinates'][0])**2) + ((tempY - datat['geometry']['coordinates'][1])**2)
    distance1 = math.sqrt(distance1)
    print(distance1)