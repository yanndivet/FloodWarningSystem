from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """implement a function that returns a list of tuples, where each tuple holds 
    (i) a station (object) at which the latest relative water level is over tol and 
    (ii) the relative water level at the station. 
    The returned list should be sorted by the relative level in descending order. """
    liste = []
    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() >= tol:
                liste.append((station.name, station.relative_water_level()))
    liste_finale = sorted_by_key(liste, 1, reverse=True)
    return liste_finale


def stations_highest_rel_level(stations, N):
    ''' returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest. 
    The list should be sorted in descending order by relative level. '''
    return stations_level_over_threshold(stations, 0)[:N] # subtract 10 from relative level of 10th value just to be safe


