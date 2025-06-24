from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def str_to_float(s):
    '''String to float'''
    if isinstance(s, str) and s.endswith("M"):
        return float(s[:-1])
    try:
        return float(s)
    except Exception:
        return None


def main():
    '''Run a program that displays a graph on the French campus
    and Belgium campus'''
    try:
        path = "population_total.csv"
        campus = "France"
        other_campus = "Belgium"
        lim = 2050 - 1800
        data = load(path)
        years = [year for year in data][1:lim]

        my_campus_data = data[data["country"] == campus]
        my_campus_data = my_campus_data.values.flatten()[1:lim]

        other_campus_data = data[data["country"] == other_campus]
        other_campus_data = other_campus_data.values.flatten()[1:lim]

        values1 = [str_to_float(x) for x in my_campus_data]
        values2 = [str_to_float(x) for x in other_campus_data]

        plt.plot(years, values1, label=campus)
        plt.plot(years, values2, label=other_campus)

        ytick_value = np.arange(20, max(values1 + values2))
        ytick_dict = [str(int(tick)) + "M" for tick in ytick_value]
        plt.yticks(ytick_value[::20], ytick_dict[::20])
        plt.xticks(years[::40])
        plt.title("Population Projections")
        plt.legend()
        plt.ylabel("Population")
        plt.xlabel("Year")
        plt.show()
    except Exception as e:
        print(e)
    return None


if __name__ == "__main__":
    main()
