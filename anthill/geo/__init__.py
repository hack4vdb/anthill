from data.ergebnisse import ergebnisse
from data.plz_latlon import coordinates

def get_wahlergebnis(plz):
    """
    Returns Wahlergebnis for a PLZ.
    If no result for PLZ is found, returns None.
    """
    return ergebnisse.get(plz, None)


def get_coordinates(plz):
    """
    Returns a pair of lat/lon coordinates for the center of the PLZ.
    When PLZ is not found, returns the center coordinates of Austria.
    """
    return coordinates.get(plz, (47.5, 14.3))
