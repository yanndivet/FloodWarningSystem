# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key
from haversine import haversine


def stations_by_distance(stations, p):
    """Given a list of station objects and a coordinate p, 
    returns a list of (station, distance) tuples, 
    where distance (float) is the distance of the station (MonitoringStation) from the coordinate p."""
    list_stations = []
    for station in stations:
        list_stations.append((station.name, haversine(station.coord, p)))
    list_stations = sorted_by_key(list_stations, 1)
    return list_stations

def stations_within_radius(stations, centre, r):
    """ returns a list of all stations within radius r of a geographic coordinate x """
    stations_within_R = []
    for station in stations:
        if haversine(station.coord, centre) <= r :
            stations_within_R.append((station.name, haversine(station.coord, centre))) 
    return sorted(stations_within_R)

def rivers_with_station(stations):
    """given a list of station objects, returns a container (list/tuple/set) with the names
       of the rivers with a monitoring station.
    """
    rivers_with_st = set()
    for station in stations:
        rivers_with_st.add(station.river)
    return sorted(rivers_with_st)

def stations_by_river(stations):
    """returns a dictionary that maps river names to a list of station objects on a given river.
    """
    st_by_river = {}
    for river in rivers_with_station(stations):
        liste = []
        for station in stations:
            if station.river == river:
                liste.append(station.name)
        st_by_river[river] = liste
    return st_by_river 
    
    

