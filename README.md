Project Overview
The Build Dependency Resolver is a program that determines the correct order to build files when some files depend on others. In many software projects one file cannot be built unless another required file is built first.
This project ensures files are built in the correct order and also detects circular dependencies which can cause build failures.
Project Objectives
The main objective is to understand how file dependency systems work in software development. It aims to teach how dependencies can be represented using graphs and how topological sorting can be applied to determine the correct build order. It also focuses on detecting circular dependencies, which can cause errors during the build process. Overall, it helps simulate how real-world build systems manage file compilation in an organized and efficient way.
Problem Description
If File A depends on File B, then File B must be built before File A.
This dependency is represented as:
B → A, This means  B is built first, followed by A.
 
Data Structures and Algorithms Used
This project uses three main data structures:
•	Graph (Adjacency List)
Stores file dependencies as directed edges.
•	In-Degree Array
Tracks how many dependencies each file has. Files with 0 dependencies are ready to build.
•	Queue
Stores files that are ready to be built and ensures correct processing order.
 
This project uses Topological Sorting or Kahn’s Algorithm to find the correct order in which files should be built. The algorithm starts by counting the number of dependencies for each file. Files that have no dependencies are then placed into a queue, since they are ready to be built first. The program processes these files one at a time and removes their dependency links from other files. As each dependency is removed the dependency counts of the remaining files are updated. If the process reaches a point where no file has zero dependencies but some files are still not built the system identifies this as a circular dependency and reports an error.
Supported Commands
DEPENDS <A> <B>
Declares that File A depends on File B
Example: DEPENDS Main Utils
BUILD
Generates the correct build order or reports a circular dependency error.

Conclusion
This project demonstrates how graphs and topological sorting can solve real-world dependency problems. It ensures correct build order and prevents errors caused by circular dependencies.

