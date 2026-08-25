
seats = [   [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

print("==CINEMA SEAT CHART ==")

for row in seats:
    print(" | ".join(str(seat) for seat in row))

row = int(input("\nEnter row (1-4): "))
column = int(input("Enter column (1-5): "))

row -= 1
column -= 1

if row < 0 or row >= 4 or column < 0 or column >= 5:
    print("Invalid seat position!")

elif seats[row][column] == "R":
    print("Sorry, that seat is already reserved!")

# Reserve the seat
else:
    seats[row][column] = "R"
    print("Seat reserved successfully!")

print("\n==UPDATED CHART===")

for row in seats:
    print(" | ".join(str(seat) for seat in row))