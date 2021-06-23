# GridHub solves Smart Grid
## Introduction
Smart Grid is a case where 150 houses and 5 batteries are distributed on a 50x50 grid. Each house contains solars panels that have a distinctive output and each battery has a max capacity to hold 1507 output. Houses are connected to a battery with a cable. This cable has a certain cost of 9 per grid-segment. Each battery also has a cost of 5000, which remains constant for now.












--------------------------------------------------------------------------------------------------------------------------------
#### OUR RESEARCH
--------------------------------------------------------------------------------------------------------------------------------

##### OPTIMIZATION GOAL
Our goal is to match each house to a battery doing this in the most efficient way to minimize the total cost by implementing different algorithmes.

##### TOTAL COST
TC = LEN(grid-segment) * 9 + 5 * BAT price

##### RESTRICTIONS
- Batteries may not be connected to each other 
- Each house can only be connected with 1 battery 
- Each hose has a unique cable to the battery 
- Multiple calbles can be placed on the same grid segments, but these cables must be unique.

### OUTPUT



### ASSIGNMENT INFO
For the first assignments we have three dummy District assigned to us (see /data).

### ASSIGNMENT 1
- Connect each house in District 1 with a battery accounting for the MAX cap of the Batteries.

### ASSIGNMENT 2
- Calculate the cost of Assignment 1 and try to optimize this SmartGrid (lowering the cost).

### ASSIGNMENT 3 WITH A CHANGE IN RESTRICTIONS
restriction update: Houses may now share cables.
- Connect each house in the three districs with a battery accounting for the MAX cap of the Batteries.

### ASSIGNMENT 4
- OPTIMIZE the SmartGrid for each of the three districts. 


## ADVANCED
