from connect4 import Connect4
from typing import Tuple, List

def minimax(game:Connect4, player:str, max_depth:int = 5, cur_depth:int = 0) -> Tuple[int, int]:
    is_over, winner = game.is_terminal()
    if is_over:
        if winner == "O":
            return 1000, None
        elif winner == "X":
            return -1000, None
        elif winner == "Tie":
            return 0, None
        
    if player == "max":
        max_eval = float("-inf")
        max_action = None

        for a in game.actions():
            sub_game = Connect4(game.state(), game.to_move())
            sub_game.make_move(a)

            c_eval, _ = minimax(sub_game, "min", max_depth, cur_depth+1)
            if c_eval > max_eval:
                max_eval = c_eval
                max_action = a
        return max_eval, max_action
    



