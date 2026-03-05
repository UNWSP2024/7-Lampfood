#Elliott Morris, 2/18/2026, Rain.py

def main():
    months = ("January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December")

    rainfall = []

    #Get rainfall for each month
    for month in months:
        amount = float(input(f"Enter the total rainfall for {month}: "))
        rainfall.append(amount)

    #Calculate total and average rainfall
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / len(months)

    #Find the highest and lowest
    highest_month = months[rainfall.index(max(rainfall))]
    lowest_month = months[rainfall.index(min(rainfall))]

    #display results
    print("\nRainfall Statistics:")
    print(f"Total rainfall for the year: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Month with the highest rainfall: {highest_month}")
    print(f"Month with the lowest rainfall: {lowest_month}")

if __name__ == "__main__":
    main()
