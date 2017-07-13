import json, os, sys

filepath = sys.argv[1]

def load_data(filepath):

   if not os.path.exists(filepath):
    return None
   with open(filepath, 'r') as file_handler:
    return json.load(file_handler)

def get_biggest_bar(data):
    
    SeatsCount = {}
    for bar in data:
        SeatsCount[bar["global_id"]]=bar["SeatsCount"]
    return(sorted(SeatsCount, key=lambda x: int(SeatsCount[x]), reverse=True )[0])
    
def get_smallest_bar(data):

    SeatsCount = {}
    for bar in data:
        if bar["SeatsCount"]>2:
            SeatsCount[bar["global_id"]]=bar["SeatsCount"]

    return(sorted(SeatsCount, key=lambda x: int(SeatsCount[x]), reverse=False )[0])
   
def get_closest_bar(data, longitude, latitude):

    DistanceCount = {}
    for bar in data:
        DistanceCount[bar["global_id"]]=distance(longitude, latitude , x2=float(bar["Longitude_WGS84"]),y2=float(bar["Latitude_WGS84"]))
        
    return(sorted(DistanceCount, key=lambda x: float(DistanceCount[x]), reverse=False )[0])
     
def distance(x1, y1, x2, y2):
    return(((x2-x1)**2 + (y2-y1)**2)**0.5)

if __name__ == '__main__':
    
    try:
        latitude = float(input('Enter Latitude: '))
        longitude = float(input('Enter Longitude: '))
    except ValueError:
        latitude = None
        longitude = None

    if (latitude or longitude) is None:
        print('Error! Check your input!')

    data=load_data(filepath)

    for bar in data:
        if bar["global_id"] == get_biggest_bar(data):
            print('The biggest bar is ', bar["Name"], bar["Address"],'seats:',bar["SeatsCount"])
        
        if bar["global_id"] == get_smallest_bar(data):
            print('The smallest bar is ', bar["Name"], bar["Address"],'seats:',bar["SeatsCount"])

        if bar["global_id"] == get_closest_bar(data,longitude, latitude):
            print('The nearest bar is ', bar["Name"], bar["Address"],'seats:',bar["SeatsCount"])
        
    print('Have a nice evening!')
    