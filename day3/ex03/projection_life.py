from load_csv import load
import matplotlib.pyplot as plt
import sys

def main():
    """
    Loads and visualizes the correlation between Gross National Product (GNP)
    and life expectancy in the year 1900 using a scatter plot.
    Handles file loading errors gracefully.
    """
    try:
        income_file = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        life_file = "life_expectancy_yars.csv"
        
        income_data = load(income_file)
        if income_data is None:
            sys.exit(1)
            
        life_expectancy_data = load(life_file)
        if life_expectancy_data is None:
            sys.exit(1)

        year_1900_column = '1900'
        gnp_1900 = income_data[year_1900_column]
        life_expectancy_1900 = life_expectancy_data[year_1900_column]

        plt.figure(figsize=(10, 6))
        plt.scatter(gnp_1900, life_expectancy_1900)
        plt.title("Year 1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()

    except KeyError:
        print(f"Error: Missing '1900' column in one of the datasets")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()