from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        path1 = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        path2 = "life_expectancy_years.csv"
        year = 1900
        inflation_data = load(path1)
        life_expectancy_data = load(path2)

        values1 = inflation_data[[str(year)]].values.flatten()
        values2 = life_expectancy_data[[str(year)]].values.flatten()

        plt.scatter(values1, values2)
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.title(year)
        plt.ylabel("Life Expectancy")
        plt.xlabel("Gross domestic product")
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
