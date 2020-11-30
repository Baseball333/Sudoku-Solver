# Sudoku-Solver
This project is a sudoku solver I wrote in Python in September 2019, employing the backtracking algorithm.

First commit:
This is the official initialization of the Python sudoku solver. This project was originally written in September 2019 with the intention of implementing the "backtracking" algorithm. Although backtracking is commonly regarded among programmers I will account those who are not familiar and explain backtracking to them. To comprehend backtracking a programmer must be aware of the "naive algorithm".

Second commit:
The naive algorithm is a manner of representing quantities by selecting every possible value from 1-9. The naive algorithm's application is especially evident in sudoku, where possible solutions to blank spaces are often employed usingr the naive algorithm. Although the naive algorithm remains a viable solution to such problems, it is computationally inefficient. Note how most of the programmers which apply the naive algorithm are unaware of backtracking's algorithm.
lev
Third commit: 
By contrast, backtracking was an algorithm created to preserve computational efficiency and arrive at a solution. At its fundamental level backtracking is the process of adding nodes in a possible solution and eliminating all nodes which do not satisfy a valid solution. After elimination of a node the previous solution is validated and this process repeats incrementally. Akin to the naive algorithm, backtracking is also applied through sudoku. Sudoku's nature is quite optimal
for the application of backtracking which is what this project is based upon.
