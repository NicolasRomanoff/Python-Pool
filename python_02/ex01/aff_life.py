from load_csv import load
import matplotlib.pyplot as plt


def main():
    '''Run a program that displays a graph on the French campus'''
    try:
        path = "life_expectancy_years.csv"
        campus = "France"

        data = load(path)
        years = [year for year in data]
        my_campus_data = data[data["country"] == campus].values.flatten()

        plt.plot(years[1:], my_campus_data[1:])
        plt.xticks(years[1::40])
        plt.title(f"{campus} Life expectancy Projections")
        plt.ylabel("Life expectancy")
        plt.xlabel("Year")
        plt.show()
    except Exception as e:
        print(e)
    return None


if __name__ == "__main__":
    main()
