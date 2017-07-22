import json
import os
import sys


def load_bar_information(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(bar_information):
    return max(bar_information, key=lambda x: x["SeatsCount"])


def get_smallest_bar(bar_information):
    return min(bar_information, key=lambda x: x["SeatsCount"])


def get_closest_bar(bar_information, longitude, latitude):
    return min(bar_information, key=lambda x: distance(longitude, latitude, coordx2=float(x["Longitude_WGS84"]), coordy2=float(x
["Latitude_WGS84"])))


def distance(coordx1, coordy1, coordx2, coordy2):
    return ((coordx2 - coordx1)**2 + (coordy2 - coordy1)**2)**0.5


def get_bar_information(bar_json):
    print(bar_json["Name"], bar_json["Address"],
          'seats:', bar_json["SeatsCount"])


if __name__ == '__main__':
    jsonfile = sys.argv[1]
    if not os.path.exists(jsonfile):
        print("Error! Check your JSON file!")
    else:
        try:
            jsonfile = sys.argv[1]
            os.path.exists(jsonfile)
            your_latitude = float(input('Enter Latitude: '))
            your_longitude = float(input('Enter Longitude: '))
        except ValueError:
            print('Error! Check your geo position input!')
        else:
            bar_info = load_bar_information(jsonfile)
            biggest = get_biggest_bar(bar_info)
            smallest = get_smallest_bar(bar_info)
            closest = get_closest_bar(bar_info, your_longitude, your_latitude)
            print('The biggest is')
            get_bar_information(biggest)
            print('The smallest is')
            get_bar_information(smallest)
            print('The closest is')
            get_bar_information(closest)
