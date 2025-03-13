from load_csv import load
import matplotlib.pyplot as plt

def main():
    """
    Loads life expectancy data, filters for Lebanon's data, and plots a line graph.
    If the file or data for the specified country is not found, prints an error and exits.
    """
    dataset = load("life_expectancy_years.csv")
    
    if dataset is None:
        return

    country_name = 'Lebanon'
    country_data = dataset[dataset['country'] == country_name]

    if country_data.empty:
        print(f"Error: No data found for country '{country_name}'. Please check the country name.")
        return

    years = country_data.columns[1:].to_numpy(dtype=int)
    life_expectancy = country_data.values[0][1:]

    plt.plot(years, life_expectancy, label=country_name)
    plt.title(f'Life Expectancy in {country_name} Over the Years')
    plt.xlabel('Year')
    plt.xticks(years[::40], rotation=45)
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 101, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
