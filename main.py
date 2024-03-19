import pandas as pd
from thermalzone import get_all_thermal_zones, get_all_temperatures, get_temperature, save_thermal_temperature
from thermalzone import load_temperature_data, plot_temperature_graph

if __name__ == "__main__":
    
    df = load_temperature_data()
    day_to_plot = input("Digite o dia que deseja plotar (YYYY-MM-DD): ")

    plot_temperature_graph(df, day_to_plot)