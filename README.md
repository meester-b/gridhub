# GridHub solves Smart Grid
## CASE INTRODUCTION
SmartGrid is a case where 150 houses and 5 batteries are distributed on a 50x50 grid. Each house contains solars panels that have a distinctive output and each battery has a max capacity of 1507 to hold output. Houses are connected to a battery with a cable. This cable has a certain cost of 9 per grid-segment. Each battery also has a cost of 5000, which remains constant for now.

#### Case restrictions
- Batteries may not be connected to each other 
- Each house can only be connected with 1 battery 
- Each hose has a unique cable to the battery 
- Multiple calbles can be placed on the same grid segments, but these cables must be unique.

The total output of all houses just barely fits in the total capacity of all batteries, which makes it difficult to create a configuration in which all houses are connected, but also to optimize the grid without breaking constraints. The assignment was created in different steps that are shown below.

### Assignment information
For the first assignments we have three dummy districts assigned to us (see /data).

1. Connect each house in District 1 with a battery accounting for the maximum capacity of the batteries.

2. Calculate the cost of Assignment 1 and try to optimize this SmartGrid (lowering the cost).

Restriction update: Houses may now share cables.

3. Connect each house in the three districs with a battery accounting for the maximum capacity of the batteries.

4. Optimize the SmartGrid for each of the three districts. 

Our ultimate goal is to match each house to a battery, and doing this in the most efficient way by implementing different algorithms. This will hopefully minimize the total cost. The total cost will be calculated using the following formula:

TC = len(all grid-segments) * 9 + 5 * battery price


## THE RESEARCH
### Random algorithm

#### Results

### Greedy algorithm

#### Results

### Hillclimber algorithm

#### Results

### Simulated Annealing algorithm

#### Results

### Iterative algorithm

#### Results


## REPLICATE THE RESULTS
It is strongly recommended to use Visual Studio Code to run this programme. The programme requires Python to be installed.

Run:
```
sudo apt install python3-pip
```
This will install pip.

Run:
```
pip install -r requirements.txt
```
This will install all necessary packages for this programme.

Run `python3 main.py` in the VSCode terminal to start. You will be prompted for several options:
- Which district do you want to work with? 1/2/3 and press Enter
- Do you want to allow cable sharing? Y/N and press Enter
- Do you want to respect the constraints? Y/N and press Enter
- How many times do you want to run your chosen algorithm(s)? Any integer above 1 and press Enter
Depending on your choices, you will get options for which algorithm and improvement algorithm you want to run.