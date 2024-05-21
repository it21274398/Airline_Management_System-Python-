# DSA Assignment

## Description
This project demonstrates the use of BFS, hashing, and heap sort to solve a real-world problem in an airline management system. It includes the implementation of these algorithms and their integration to find, store, and sort flight routes.

## Files
- `graph.py`: Contains the `Graph` class and BFS implementation.
- `hash_table.py`: Contains the `HashTable` class for airport lookup.
- `heap_sort.py`: Contains the heap sort implementation for route sorting.
- `main.py`: Main script to run the program.

## Dependencies
- Python 3.x

## How to Run
1. Ensure you have Python installed on your system.
2. Save all the code files (`graph.py`, `hash_table.py`, `heap_sort.py`, `main.py`) in the same directory.
3. Open a terminal or command prompt in that directory.
4. Run the command `python main.py` to execute the program.
5. Follow the on-screen instructions to see the results of the BFS, hash table operations, and sorted routes.

## Test Data
- Sample graph edges:
  - A -> B: 100 km
  - A -> C: 200 km
  - B -> C: 150 km
  - C -> D: 100 km
- Sample hash table entries:
  - 'JFK': 'John F. Kennedy International Airport'
  - 'LAX': 'Los Angeles International Airport'
- Sample routes for sorting:
  - Route 1: ['A', 'B', 'D'], Distance: 200 km
  - Route 2: ['A', 'C', 'D'], Distance: 300 km
  - Route 3: ['A', 'B', 'C', 'D'], Distance: 250 km
