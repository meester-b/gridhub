## Development Code
In this folder we have some code that we have worked on, but we sadly did not manage to get it to function properly. The code in this folder can NOT be run from main.py and can NOT yet be tested on functionality.

### Iterative algorithm
The iterative algorithm tries to improve the grid that results from our Greedy with shared cables algorithm. It searches the grid for the longest cables that are present, and cuts those cables off. This results in a cluster of houses that is not connected to any battery anymore, but belonged to a certain battery previously. The final step is then to take this cluster and find the shortest distance from any of the houses in that cluster to any house point that is connected to the specific battery the cluster was disconnected from.