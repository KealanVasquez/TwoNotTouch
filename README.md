# TwoNotTouch
A puzzle is a string of 100 characters, each character one of the letters from A to J. The research conducted with these algorithms were from a published set of puzzles from krazydad.com, so those puzzles are not published here. 

The file "BoardUI" is an implementation of the Two Not Touch grid into python, allowing one to find missing logical inferences when the Human Algorithm leaves an instance of the puzzle partially unsolved.

The file "LINGO input generator" takes a puzzle and outputs the ten region constraints that can be added to the row, column, and adjacency constraints in a LINGO file. 

The file "Backtracking" solves the puzzles through exhaustion and pruning.

The file "Human Algorithm" solves the puzzles via logical inferences implemented by the author. It can be improved upon by adding further logic.

The file "Human + Backtrack Comparison" runs both human and backtracking algorithms on a full set of puzzles, and compares their solving times, also including an estmiated line for the times of the LINGO solver.
