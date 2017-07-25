import json
import os
import sys


def load_bar_information(filepath):
    try:
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    except json.JSONDecodeError:
        print("Error! This is not JSON format file!")
        exit()

def get_biggest_bar(bar_information):
    return max(bar_information, key=lambda x: x["SeatsCount"])


def get_smallest_bar(bar_information):
    return min(bar_information, key=lambda x: x["SeatsCount"])


def get_closest_bar(bar_information, longitude, latitude):
    return min(bar_information, key=lambda x: distance(longitude, latitude, coordx2=float(x["Longitude_WGS84"]), coordy2=float(x
["Latitude_WGS84"])))


def distance(coordx1, coordy1, coordx2, coordy2):
    return ((coordx2 - coordx1)**2 + (coordy2 - coordy1)**2)**0.5


def print_bar_information(bar_json):
    print(bar_json["Name"], bar_json["Address"],
          'seats:', bar_json["SeatsCount"])


if __name__ == '__main__':

    if not len(sys.argv) > 1:
        print("Error: Empty argument, try bars.py <filename>")
        exit()
    jsonfile = sys.argv[1]
    if not os.path.exists(jsonfile):
        print("Error! File doesn't exist!")
        exit()
    try:
        your_latitude = float(input('Enter Latitude: '))
        your_longitude = float(input('Enter Longitude: '))
    except ValueError:
        print('Error! Check your geo position input!')
        exit()
    bar_info = load_bar_information(jsonfile)
    biggest = get_biggest_bar(bar_info)
    smallest = get_smallest_bar(bar_info)
    closest = get_closest_bar(bar_info, your_longitude, your_latitude)
    print('The biggest is')
    print_bar_information(biggest)
    print('The smallest is')
    print_bar_information(smallest)
    print('The closest is')
    print_bar_information(closest)
