from anthill.geo.data.ergebnisse import ergebnisse
from anthill.geo.data.plz_latlon import coordinates
from anthill.geo.data.ortezumflyern import orte
from geopy.distance import great_circle

def get_wahlergebnis(plz):
    """
    Returns Wahlergebnis for a PLZ.
    If no result for PLZ is found, returns None.
    """
    return ergebnisse.get(int(plz), None)


def get_coordinates(plz):
    """
    Returns a pair of lat/lon coordinates for the center of the PLZ.
    When PLZ is not found, returns the center coordinates of Austria.
    """
    return coordinates.get(int(plz), (47.5, 14.3))


def get_nearest_ortzumflyern(plz):
    """
    Returns a the nearest location for a meetup from our "cool places to
    create meetups"-file
    """
    plz_latlon = get_coordinates(plz)
    min_idx = 0
    min = 99999
    for i in range(len(orte)):
        ort_latlon = (orte[i]['lat'], orte[i]['lon'])
        dist = great_circle(plz_latlon, ort_latlon).meters
        if dist < min:
            min = dist
            min_idx = i
    return (min_idx, orte[min_idx])
