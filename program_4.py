#Elliott Morris, 2/21/2026, coordinates.py

import math

#function to calculate the distance
def distance(p1, p2):

    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

def main():
    try:
        #get user input
        print("Enter the first 3d Coordinate:")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        z1 = float(input("z1: "))

        print("Enter the second 3d Coordinate:")
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        z2 = float(input("z2: "))

        #call the distance function
        dist = distance((x1, y1, z1), (x2, y2, z2))

        print("\nDistance between the two points: ", dist)

    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print("An unexpected error occured:", e)

if __name__ == "__main__":
    main()
