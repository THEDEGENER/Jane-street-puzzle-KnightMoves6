# jane street puzzle

# map A, B, C to integers

# Given a correct solution starting point the algorithum can be extremely quick, however given a random starting condition
# the algorithum can take at worst case 8^d where 8 is the number of moves and d is the total number of squares which
# is an astronimical number at worst case. There is pruning involved where the score exceeds 2024 but even then it was taking 
# way to long,

## inutituion for improvment

# given that a valid solution has a starting point between 1 - 50 distinct integers and the score is either incramented via addition 
# or multiplication then we can determine the upper bound for where a distinct integer would produce a score above 2024 early
# # we could also keep track of the number of backtracks to switch to another distinct integer, even thought this isnt a completely 
# logical pruning technique, stumbling uppon a constrained upper bounds has a much higher likelyhood than the 10 quadrillion years
# for a pure backtracking brute force in worst case time for each distinct integer

import os

mapping = {
    "a": 2,
    "b": 3,
    "c": 4
}   
board = [
    ["a", "b", "b", "c", "c", "c"],
    ["a", "b", "b", "c", "c", "c"],
    ["a", "a", "b", "b", "c", "c"],
    ["a", "a", "b", "b", "c", "c"],
    ["a", "a", "a", "b", "b", "c"],
    ["a", "a", "a", "b", "b", "c"]
]
possible_moves = (
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
)
starting_pos = (0, 0)
current_pos = starting_pos
seen_pos = [starting_pos]
end_pos = (5, 5)
score = mapping["a"]

def main():
    return solution(current_pos, score, seen_pos)

def valid_move(pos, move, seen):
    """ Validates the new position """
    new_pos = (pos[0] + move[0], pos[1] + move[1])
    if new_pos not in seen and 0 <= new_pos[0] < 6 and 0 <= new_pos[1] < 6:
        return True
    return False


def update_score_and_seen(score, current_pos, last_pos, seen):
    """ Returns the new state to allow the recursive function to manage its own state instead of a global state """
    row1, col1 = last_pos
    row, col = current_pos
    if board[row][col] == board[row1][col1]:
        new_score = score + mapping[board[row][col]]
    else:
        new_score = score * mapping[board[row][col]]
    new_seen = seen + [current_pos]
    return new_score, new_seen



def solve(current_pos, score, seen, counter):
    """ Recursive backtracking function that accepts an initial state and then manages the state internally
        meaning the state dosent need to be reverted but rather if an outcome doesnt meet the 
        conditions the loop continues"""
    
    ### Based on the implementation of the sudoku solver ### 

    # Base case: solution found
    if current_pos == end_pos and score == 2024:
        return current_pos, score, seen

    for move in possible_moves:
        if valid_move(current_pos, move, seen) and score < 2024: # inital check for a score less than 2024 is still valid because it doesnt prune the branch immediatly
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            new_score, new_seen = update_score_and_seen(score, new_pos, current_pos, seen)
            
            # Prune branch if new_score exceeds 2024, this is a more immediate approach

            if new_score > 2024:
                continue
            
            # slows down the printing and clearing of the console to be able to actually read the state
            counter["moves"] += 1
            if counter["moves"] % 200000 == 0:
                print(new_seen, new_score)
            result = solve(new_pos, new_score, new_seen, counter)
            if result is not None:
                return result
    return None

def solution(current_pos, score, seen_pos):
    for key in mapping.keys():
        for i in range(2, 11):
            mapping[key] = i
            counter = {"moves": 0}  
            result = solve(current_pos, score, seen_pos, counter)
            if result is not None:
                print("Found solution:", result, mapping.values())
                break
        else:
            print("No solution possible")

if __name__ == "__main__":
    main()
    
    




    


    



        


    