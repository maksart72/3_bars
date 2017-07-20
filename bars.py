import json
import os
import sys


def load_bar_information(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(bar_information):
    return max((bar['SeatsCount'], bar['global_id']) for bar in bar_information)


def get_smallest_bar(bar_information):
    return min((bar['SeatsCount'], bar['global_id']) for bar in bar_information)
    
def get_closest_bar(bar_information, longitude, latitude):
    return min((distance(longitude, latitude, coordx2=float(bar["Longitude_WGS84"]), coordy2=float(bar["Latitude_WGS84"])), bar['global_id']) for bar in bar_information)

def distance(coordx1, coordy1, coordx2, coordy2):
    return ((coordx2 - coordx1)**2 + (coordy2 - coordy1)**2)**0.5


def print_results(filepath):
    bar_information = load_bar_information(filepath)
    for bars in bar_information:
        if bars["global_id"] == get_biggest_bar(bar_information)[1]:
            print('The biggest bar is ',
                  bars["Name"], bars["Address"], 'seats:', bars["SeatsCount"])

        if bars["global_id"] == get_smallest_bar(bar_information)[1]:
            print('The smallest bar is ',
                  bars["Name"], bars["Address"], 'seats:', bars["SeatsCount"])

        if bars["global_id"] == get_closest_bar(bar_information, your_longitude, your_latitude)[1]:
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
