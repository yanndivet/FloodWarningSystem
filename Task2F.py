from lib2to3.pgen2.tokenize import StopTokenizing
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
import datetime
import matplotlib 
from floodsystem.utils import sorted_by_key
import matplotlib.pyplot as plt



'''def run():
    stations = build_station_list() 
    update_water_levels(stations)
    stations_by_water_level = []
    for station in stations:
        if station.latest_level == None:
            pass
        else:
            stations_by_water_level.append((station.name, station.latest_level))
    sorted_list = sorted_by_key(stations_by_water_level, 1, True)[:5]
    name_list = []
    for i in range(5):
        name_list.append(sorted_list[i][0])
    print(sorted_list)

    for station in stations:
        for item in range (5):
            if station.name == name_list[item]:
                print(station.name)
                dates, levels = fetch_measure_levels(station.measure_id,dt = datetime.timedelta(days = 2))    
                plot_water_level_with_fit(station, dates, levels, p=4)'''


def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest_5 = sorted(((station, station.relative_water_level()) for station in stations if station.relative_water_level() != None), key = lambda x: x[1], reverse = True)[:5]
    print(highest_5)
    for i in highest_5:
        station  = i[0]
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days = dt))
        high_level = [station.typical_range[0]]*len(levels)
        low_level = [station.typical_range[1]]*len(levels)
        plt.plot(dates, high_level)
        plt.plot(dates, low_level)
        
        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()