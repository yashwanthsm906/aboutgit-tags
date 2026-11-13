
# MISSIONARIES AND CANNIBALS GAME

def display(m, c, boat):
    print("\n" + "=" * 45)
    print("       MISSIONARIES AND CANNIBALS")
    print("=" * 45)

    rm = 3 - m
    rc = 3 - c

    print("\nLEFT BANK                 RIGHT BANK")
    print("-" * 45)

    print("Missionaries:", m, " " * 12, "Missionaries:", rm)
    print("Cannibals:  ", c, " " * 12, "Cannibals:  ", rc)

    print("\nBoat position:", "LEFT" if boat == 1 else "RIGHT")
    print("=" * 45)


def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    rm = 3 - m
    rc = 3 - c

    if m > 0 and c > m:
        return False

    if rm > 0 and rc > rm:
        return False

    return True


def play_game():
    m = 3
    c = 3
    boat = 1
    moves = 0

    print("\nWELCOME TO THE GAME!")
    print("Move all missionaries and cannibals safely.")
    print("Boat capacity: Maximum 2 people")
    print("Enter 1 or 2 missionaries and 0 to 2 cannibals.")
    print("At least one person must travel.")

    while True:

        display(m, c, boat)

        if m == 0 and c == 0:
            print("\nCONGRATULATIONS!")
            print("You won the game!")
            print("Total moves:", moves)
            break

        print("\nEnter the number of people to move:")

        try:
            mm = int(input("Missionaries: "))
            cc = int(input("Cannibals: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if mm + cc < 1 or mm + cc > 2:
            print("Invalid move! Boat can carry 1 or 2 people.")
            continue

        if mm > m or cc > c if boat == 1 else False:
            print("Not enough people on this bank!")
            continue

        if boat == 0 and (mm > 3-m or cc > 3-c):
            print("Not enough people on this bank!")
            continue

        if boat == 1:
            new_m = m - mm
            new_c = c - cc
            new_boat = 0
        else:
            new_m = m + mm
            new_c = c + cc
            new_boat = 1

        if not is_valid(new_m, new_c):
            print("\nINVALID MOVE!")
            print("Cannibals cannot outnumber missionaries.")
            print("Try another move.")
            continue

        m = new_m
        c = new_c
        boat = new_boat
        moves += 1

        print("\nMove successful!")


play_game()
