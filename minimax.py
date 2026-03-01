from connect4 import Connect4
from typing import Tuple, List

def minimax(game:Connect4, player:str, max_depth:int = 5, cur_depth:int = 0, alpha:int = -2000, beta:int = 2000) -> Tuple[int, int]:
    is_over, winner = game.is_terminal()
    if is_over:
        if winner == "O":
            return 1000, None
        elif winner == "X":
            return -1000, None
        elif winner == "Tie":
            return 0, None

    if cur_depth >= max_depth:
        return heuristic(game), None
        
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
                alpha = max(max_eval, c_eval)
                if beta <= alpha:
                    break
        return max_eval, max_action
    
    if player == "min":
        min_eval = float("inf")
        min_action = None

        for a in game.actions():
            sub_game = Connect4(game.state(), game.to_move())
            sub_game.make_move(a)

            c_eval, _ = minimax(sub_game, "max", max_depth, cur_depth+1)
            if c_eval < min_eval:
                min_eval = c_eval
                min_action = a
                beta = min(min_eval, c_eval)
                if beta <= alpha:
                    break
        return min_eval, min_action
    
def heuristic(game:Connect4) -> int:
    val = 0
    for row in game.board:
        val += 2^row.count("O") - 2^row.count("X")
    return val

    



