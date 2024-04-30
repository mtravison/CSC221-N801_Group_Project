# Clerick Barrion, Benjamin Ferrell, Giancarlo Kite, Matthew Travison, and Alyssa Vang 
# May 2, 2024 project1_group4.py

# Import module example
import matplotlib.pyplot
# import modules.visualization as visualization
import modules.stats as stats

# declare constants
EARLIEST_YEAR = 2012
LATEST_YEAR = 2022
YEAR_OPTIONS = ( ["1", "2"], ["Single Year", "Range of Years"] )

# Uses the function stats.py inside the modules folder
deaths_by_year = stats.deaths_by_year()
drug_distribution_by_year = stats.drug_distribution_by_year(2014)

print(deaths_by_year[2020])
print(drug_distribution_by_year)

# ================================  call functions in looped sequence
def main():
    while True:
        print("Connecticut Accidental Drug Related Death Data ")
        print("1. Compare State Comparisons")
        print("2. Monthly Chart in Multiple States")
        print("3. Total Cases of Percentage Deaths")
        print("4. Monthly Data in Single States")
        print("5. Monthly Data in Multiple States")
        print("6. Exit")

        choice = input("Enter your choice: ") 
        
        if choice == "1":
            data_range = input_range()
        elif choice == "2":
            data_range = input_range()
        elif choice == "3":
            data_range = input_range()
        elif choice == "4":
            data_range = input_range()
        elif choice == "5":
            data_range = input_range()        
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# ================================  input a valid single year or range of years to chart
def input_range():
    print("\nWould you like to graph data for a single year or a range of years?")
    for i in range(len(YEAR_OPTIONS[0])):
        print(f"{YEAR_OPTIONS[0][i]}. {YEAR_OPTIONS[1][i]}")
    single_or_multi = input("Your selection: ")
    
    # input validation
    if single_or_multi not in YEAR_OPTIONS[0]:
        input("\tPlease choose a valid menu option\n\tPress enter to continue...")
        return input_range()
    # single year selected
    elif single_or_multi == YEAR_OPTIONS[0][0]:
        year = [get_year(f"\nPlease enter a year between {EARLIEST_YEAR} and {LATEST_YEAR}: ")]
        return year
    # multiple years selected
    else:
        print(f"\nPlease enter two years between {EARLIEST_YEAR} and {LATEST_YEAR}")
        first_year = get_year("First year: ")
        last_year = get_year("Last year: ")
        return [first_year, last_year]

# ================================  input a numeric year, within a defined range
def get_year(prompt):
    try:
        year = int(input(prompt))
    except ValueError:
        input("\tPlease enter a numeric year (YYYY)\n\tPress enter to try again...")
        return get_year()
    else:
        if year not in range(EARLIEST_YEAR, LATEST_YEAR):
            input(f"\tNo data available for {year}\n\tPress enter to try again...")
            return get_year()
        else:
            return year

# ================================  call the main function
if __name__ == "__main__":
    main()