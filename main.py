import random
import time

def playagain():
    new = input("Do you want to play again? (y/n)")
    if new.lower() == "y":
        print("\n")
        newgame()

    if new.lower() == "n":
        exit()

    else:
        print("Wrong anser!")
        playagain()


def check(rows):
    if rows[0][0] == 'X' and rows [0][1] == 'X' and rows[0][2] == 'X':
        return "X"

    elif rows[1][0] == 'X' and rows [1][1] == 'X' and rows[1][2] == 'X':
        return "X"

    elif rows[2][0] == 'X' and rows [2][1] == 'X' and rows[2][2] == 'X':
        return "X"

    elif rows[0][0] == 'X' and rows[1][0] == 'X' and rows[2][0] == 'X':
        return "X"

    elif rows[0][1] == 'X' and rows[1][1] == 'X' and rows[2][1] == 'X':
        return "X"

    elif rows[0][2] == 'X' and rows[1][2] == 'X' and rows[2][2] == 'X':
        return "X"

    elif rows[0][0] == 'X' and rows[1][1] == 'X' and rows[2][2] == 'X':
        return "X"

    elif rows[0][2] == 'X' and rows[1][1] == 'X' and rows[2][0] == 'X':
        return "X"

    elif rows[0][0] == 'O' and rows[0][1] == 'O' and rows[0][2] == 'O':
        return "O"

    elif rows[1][0] == 'O' and rows[1][1] == 'O' and rows[1][2] == 'O':
        return "O"

    elif rows[2][0] == 'O' and rows[2][1] == 'O' and rows[2][2] == 'O':
        return "O"

    elif rows[0][0] == 'O' and rows[1][0] == 'O' and rows[2][0] == 'O':
        return "O"

    elif rows[0][1] == 'O' and rows[1][1] == 'O' and rows[2][1] == 'O':
        return "O"

    elif rows[0][2] == 'O' and rows[1][2] == 'O' and rows[2][2] == 'O':
        return "O"

    elif rows[0][0] == 'O' and rows[1][1] == 'O' and rows[2][2] == 'O':
        return "O"

    elif rows[0][2] == 'O' and rows[1][1] == 'O' and rows[2][0] == 'O':
        return "O"

    elif "_" not in rows[0] and "_" not in rows[1] and "_" not in rows[2]:
        printrows(rows)
        print("It's a draw!")
        game = False
        playagain()

    else:
        return "_"


def player(rounds):
    if rounds % 2 == 0:
        return "X"

    else:
        return "O"


def select_row(rows):

    pos = int(input("Select position to mark (1-9): "))
    if pos == 1 and rows[0][0] == "_":
        return (0, 0)

    elif pos == 2 and rows[0][1] == "_":
        return (0, 1)

    elif pos == 3 and rows[0][2] == "_":
        return (0, 2)

    elif pos == 4 and rows[1][0] == "_":
        return (1, 0)

    elif pos == 5 and rows[1][1] == "_":
        return (1, 1)

    elif pos == 6 and rows[1][2] == "_":
        return (1, 2)

    elif pos == 7 and rows[2][0] == "_":
        return (2, 0)

    elif pos == 8 and rows[2][1] == "_":
        return (2, 1)

    elif pos == 9 and rows[2][2] == "_":
        return (2, 2)

    else:
        print("You can't mark here!")
        return select_row(rows)


def select_row_pc(rows):
    pos = random.randint(1, 9)
    if pos == 1 and rows[0][0] == "_":
        return (0, 0)

    elif pos == 2 and rows[0][1] == "_":
        return (0, 1)

    elif pos == 3 and rows[0][2] == "_":
        return (0, 2)

    elif pos == 4 and rows[1][0] == "_":
        return (1, 0)

    elif pos == 5 and rows[1][1] == "_":
        return (1, 1)

    elif pos == 6 and rows[1][2] == "_":
        return (1, 2)

    elif pos == 7 and rows[2][0] == "_":
        return (2, 0)

    elif pos == 8 and rows[2][1] == "_":
        return (2, 1)

    elif pos == 9 and rows[2][2] == "_":
        return (2, 2)

    else:
        return select_row_pc(rows)

def mark_x(pos):
    if pos == "_":
        pos = "X"

    return pos


def mark_o(pos):
    if pos == "_":
        pos = "O"

    return pos


def printrows(rows):
    for row in rows:
        print(row[0], "|", row[1], "|", row[2])


def newgame():
    rows = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
    ]

    print("T | I | C")
    print("----------")
    print("T | A | C")
    print("----------")
    print("T | O | E")
    print("\n")

    s = int(input("1 - play against computer, 2 - 2 players, 3 - how to play, 4 - exit"))

    if s == 1:
        game = True
        rnd = random.randint(0, 1)
        while game:
            printrows(rows)
            print(f"Player {player(rnd)}'s turn!")
            if player(rnd) == "X":
                selected = select_row(rows)
                p = rows[selected[0]][selected[1]]
                mark_x(p)
                rows[selected[0]][selected[1]] = mark_x(p)

            else:
                selected = select_row_pc(rows)
                p = rows[selected[0]][selected[1]]
                mark_o(p)
                rows[selected[0]][selected[1]] = mark_o(p)

            if check(rows) != "_":
                printrows(rows)
                print(f"{check(rows)} wins!")
                game = False
                playagain()

            else:
                rnd += 1

    if s == 2:
        game = True
        rnd = random.randint(0, 1)
        while game:
            printrows(rows)
            print(f"Player {player(rnd)}'s turn!")
            selected = select_row(rows)
            p = rows[selected[0]][selected[1]]
            if player(rnd) == "X":
                mark_x(p)
                rows[selected[0]][selected[1]] = mark_x(p)

            else:
                mark_o(p)
                rows[selected[0]][selected[1]] = mark_o(p)

            if check(rows) != "_":
                printrows(rows)
                print(f"{check(rows)} wins!")
                game = False
                playagain()

            else:
                rnd += 1

    if s == 3:
        print("\n")
        print("Select a position (1-9) to place your mark (O/X) on the board.")
        time.sleep(3)
        print(["1", "2", "3"])
        print(["4", "5", "6"])
        print(["7", "8", "9"])
        time.sleep(3)
        print("\n")
        print("Player with 3 of his marks in a straight line wins!")
        time.sleep(2)
        print(["X", "_", "_"])
        print(["O", "X", "_"])
        print(["O", "O", "X"])
        print("X wins")
        time.sleep(2)
        print(["_", "_", "_"])
        print(["X", "_", "X"])
        print(["O", "O", "O"])
        print("O wins")
        time.sleep(2)
        print(["_", "O", "X"])
        print(["_", "_", "X"])
        print(["_", "O", "X"])
        print("X wins")
        input("Press enter to continue...")
        newgame()

    if s == 4:
        print("Bye!")
        exit()

    else:
        print("Invalid answer")

newgame()