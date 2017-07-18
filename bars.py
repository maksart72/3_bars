import json
import os
import sys


def load_bar_information(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(bar_information):
    seats_count = {}
    for bars in bar_information:
        seats_count[bars["global_id"]] = bars["SeatsCount"]
    return sorted(seats_count, key=lambda x: int(seats_count[x]), reverse=True)[0]


def get_smallest_bar(bar_information):
    seats_count = {}
    for bars in bar_information:
        if bars["SeatsCount"] > 2:
            seats_count[bars["global_id"]] = bars["SeatsCount"]

    return sorted(seats_count, key=lambda x: int(seats_count[x]), reverse=False)[0]


def get_closest_bar(bar_information, longitude, latitude):

    distance_count = {}
    for bars in bar_information:
        distance_count[bars["global_id"]] = distance(longitude, latitude, coordx2=float(
            bars["Longitude_WGS84"]), coordy2=float(bars["Latitude_WGS84"]))
    return sorted(distance_count, key=lambda x: float(distance_count[x]), reverse=False)[0]


def distance(coordx1, coordy1, coordx2, coordy2):
    return ((coordx2 - coordx1)**2 + (coordy2 - coordy1)**2)**0.5


def print_results(filepath):
    bar_information = load_bar_information(filepath)
    for bars in bar_information:
        if bars["global_id"] == get_biggest_bar(bar_information):
            print('The biggest bar is ',
                  bars["Name"], bars["Address"], 'seats:', bars["SeatsCount"])

        if bars["global_id"] == get_smallest_bar(bar_information):
            print('The smallest bar is ',
                  bars["Name"], bars["Address"], 'seats:', bars["SeatsCount"])

        if bars["global_id"] == get_closest_bar(bar_information, your_longitude, your_latitude):
            print('The nearest bar is ',
                  bars["Name"], bars["Address"], 'seats:', bars["SeatsCount"])
    print('Have a nice evening!')


if __name__ == '__main__':
    jsonfile = sys.argv[1]
    try:
        your_latitude = float(input('Enter Latitude: '))
        your_longitude = float(input('Enter Longitude: '))
    except ValueError:
        your_latitude = None
        your_longitude = None
    if (your_latitude or your_longitude) is None:
        print('Error! Check your input!')
    print_results(jsonfile)
