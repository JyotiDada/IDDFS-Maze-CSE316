# IDDFS Maze Solver (CSE 316)

## Problem Description
This project implements Iterative Deepening Depth-First Search (IDDFS)
to determine whether a valid path exists in a 2D maze grid.

0 -> Empty cell
1 -> Wall

Movement allowed:
Up, Down, Left, Right

## Algorithm
The solution uses Iterative Deepening Depth-First Search (IDDFS),
which repeatedly applies Depth-Limited Search (DLS)
with increasing depth until:
- The target is found
- Or maximum depth is reached

## How to Run

Make sure Python 3 is installed.

Run:
python "lab 1.py"

## Complexity
Time Complexity: O(b^d)
Space Complexity: O(d)

Where:
b = branching factor
d = depth of solution

## Author
Joyti Chakraborty
ID: 232002156
CSE 316 – Artificial Intelligence Lab
