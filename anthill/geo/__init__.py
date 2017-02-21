from anthill.geo.data.ergebnisse import ergebnisse
from anthill.geo.data.ortezumflyern import orte
from anthill.geo.data.wahl_details import wahl_details
from django.contrib.gis.geos import GEOSGeometry
from geopy.distance import great_circle

def get_wahlergebnis(plz):
    """
    Returns Wahlergebnis for a PLZ.
    If no result for PLZ is found, returns None.
    """
    return ergebnisse.get(int(plz), None)


def get_nearest_ortzumflyern(coordinates):
    """
    Returns a the nearest location for a meetup from our "cool places to
    create meetups"-file
    """
    min_idx = 0
    min = 99999
    for i in range(len(orte)):
        ort_latlon = GEOSGeometry(
            'POINT(%f %f)' %
            (orte[i]['lon'], orte[i]['lat']), srid=4326)
        dist = great_circle(coordinates, ort_latlon).meters
        if dist < min:
            min = dist
            min_idx = i
    return (min_idx, orte[min_idx])


def get_wahl_details(coordinates):
    location_id, location = get_nearest_ortzumflyern(coordinates)
    for i in range(len(wahl_details)):
        if wahl_details[i]['ort'] == location['ort']:
            return wahl_details[i]
    return None


def get_ortezumflyern(idx):
    idx = int(idx)
    if idx < len(orte):
        return orte[idx]
    else:
        return orte[0]

