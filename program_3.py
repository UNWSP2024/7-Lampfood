#Elliott Morris, 2/19/2026, U.S Population.py

def sum_population_for_year(data, target_year):
    # add population for matching years
    total_population = 0
    for record in data:
        if record[0] == target_year:
            total_population += record[2]

    return total_population

def main():
    data = []

    #add records until user chooses to stop
    while True:
        print("Enter a new record")
        year = int(input("Enter year: "))
        state = input("Enter state name: ")
        population = int(input("Enter population: "))

        data.append([year, state, population])

        #ask if user wants to continue
        choice = input("Do you want to add another record? (y/n): ").lower()
        if choice != "y":
            break

    #ask for year to total
    target_year = int(input("Enter year to calculate total population: "))

    total_population = sum_population_for_year(data, target_year)

    print(f"Total population for {target_year}: {total_population}")

if __name__ == "__main__":
    main()
