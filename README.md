# Jane-street-puzzle-KnightMoves6

## Intuition 
This jane street puzzle seemed like a good candidate for a backtracking algorithum that I had attempted by creating a sudoku solver
so i set out to implement it within the constraints of this puzzle. Backtracking was a valid solution and actually ended up being 
easier than the sudoku solver because i ended up realising that the state of the branch could be managed internally by the function 
and if a deadend was reach then the for loop iterates to the next possible move and the new "state" is never passed to the revursive call


## Constraints 
* The puzzle required 3 distinct integers to be mapped to a 2d array
* the distinct integers could not be greater than 50
* each trips score must equal 2024
* each cell can only be visited once

## Problems
the implementation was valid and would eventually reach the solution but given 8 possible moves for 36 cells
the time complexity at worst case with no effective pruning is in the quintillions of years. While the branches where
pruned if the score was greater than 2024 would have drastically decreased this number and with some conservitive best case cenarios 
that number can be reduced down to 19 hours give or take. Will there are many possible improvments such as memoization and calculating some
future state based on best case scenario being greater than the score i didnt explore these improvments for now

## Solution
Ideally without alot of time invested in pruning approaches the most effective implementation was actually just testing of starting state values.
given an already ideal starting state the program can return a solution almost instantly and therefore determining that an upper bound of 10 for
any of the distinct integers would most likely exceed the score requirments, merely testing within this range and moving to the next integer if the 
program was running quite long was a more effective solution. Merely stumbling into an ideal solution is better than testing everyone for the duration of the runtime
