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
    print(plz)
    plz_latlon = get_coordinates(plz)
    ort_latlon = (orte[0]['lat'], orte[0]['lon'])
    print(plz_latlon, ort_latlon)
    print(great_circle(plz_latlon, ort_latlon).meters/1000.0)
    return orte[0]
