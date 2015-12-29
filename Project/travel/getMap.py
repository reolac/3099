import googlemaps

def get_place_id (location):
    gmaps = googlemaps.Client(key="AIzaSyBo8Y2Df9bwvkxjiE6p7uU6C5VUEhGuMus")
    geocode_result = gmaps.geocode(location +  'UK')
    f = 0
    for d in geocode_result:
        f = (d['place_id'])
        break
    return (f)

