#Elliott Morris, 2/19/2026, Greater than.py

def display_greater_than(lst,n):
    #compares values
    for num in lst:
        if num > n:
            print(num)

def main():
    #create a list of numbers
    numbers = []

    #ask user how many numbers they want to enter
    count = int(input("How many numbers would you like to add? "))

    #Get numbers from user
    for i in range(count):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)

    #Get comparison number
    n = float(input("Enter number to compare against: "))

    #print results
    print(f"\nNumbers Greater than {n}: ")
    display_greater_than(numbers,n)

if __name__ == "__main__":
    main()
