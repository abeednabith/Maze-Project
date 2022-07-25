# Maze-Project
Overview: A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block. The most important task for maze solving robots is the fast and reliable finding of its shortest path from its initial point to its final destination point. This paper proposes an intelligent maze solving robot that can determine its shortest path on a line maze based on image processing and artificial intelligence algorithms.

Usecase: There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won’t stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the ball’s start position, the destination and the maze, determine whether the ball could stop at the destination.
The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Solutions: Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally. Solving one piece at a time, and removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree) is the process of backtracking.
DFS, stands for Depth First Search. DFS uses Stack to find the shortest path
BFS, stands for Breadth First Search. BFS uses Queue to find the shortest path

Both BFS and DFS cases visit all the nodes without significant extra overhead. If the search can be aborted when a matching element is found, BFS should typically be faster if the searched element is typically higher up in the search tree because it goes level by level. DFS might be faster if the searched element is typically relatively deep and finding one of many is sufficient.
