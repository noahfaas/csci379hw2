import argparse
from connect4 import Connect4
from minimax import minimax

parser = argparse.ArgumentParser("HW 2")
parser.add_argument("-x",  choices=["human","ai"], help="Whether x is controlled by human or AI")
parser.add_argument("-o",  choices=["human","ai"], help="Whether o is controlled by human or AI")
parser.add_argument("--debug", action="store_true", help="Turns on debug mode")

if "__main__":
    args = parser.parse_args()

    game = Connect4()
    game.welcome()

    done = False
    winner = None
    while not done:
        game.display()
        if game.turn == "O":
            if args.o == "ai":
                score, move = minimax(game, "max")
                game.make_move(move)
            else:
                col = input("Player O, select a column to place a piece:")
                game.make_move(int(col))
        else:
            if args.x == "ai":
                score, move = minimax(game, "min")
                game.make_move(move)
            else:
                col = input("Player X, select a column to place a piece:")
                game.make_move(int(col))
        done, winner = game.is_terminal()

    game.display()
    print(f"{winner} wins!")