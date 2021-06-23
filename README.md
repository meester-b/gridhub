# GridHub solves SmartGrid
## Case Introduction
SmartGrid is a case where 150 houses and 5 batteries are distributed on a 50x50 grid. Each house contains solars panels that have a distinctive output and each battery has a max capacity of 1507 to hold output. Houses are connected to a battery with a cable. This cable has a certain cost of 9 per grid-segment. Each battery also has a cost of 5000, which remains constant for now.

### Case restrictions
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


## The Research
### Random algorithm
#### Random unconstrained
- Get a copy of a grid of one of the districts
- Shuffle the list of houses that are on that grid
- Loop through the houses
- For each house, select a random battery
- Connect each house to that random battery
- Calculate the total distance of cables on the grid

#### Random constrained
- Get a copy of a grid of one of the districts
- Shuffle the list of houses that are on that grid
- Loop through the houses
- For each house, select a random battery
- Connect each house to that random battery if house output is smaller than remaining capacity of the battery
- If battery is full, connect to another battery
- If all batteries are full, break out and mark as failed attempt
- Calculate the total distance of cables on the grid

### Greedy algorithm
#### Greedy unconstrained
- Get a copy of a grid of one of the districts
- Shuffle the list of houses that are on that grid
- Loop through the houses
- For each house, connect to the closest battery
- Calculate the total distance of cables on the grid

#### Greedy constrained
- Get a copy of a grid of one of the districts
- Shuffle the list of houses that are on that grid
- Loop through the houses
- For each house, connect to the closest battery
- If that battery is full, connect to the second closest battery
- Calculate the total distance of cables on the grid
- If all batteries are full, break out and mark as failed attempt
- Calculate the total distance of cables on the grid

#### Greedy unconstrained shared cables
- Get a copy of a grid of one of the districts
- Shuffle the list of houses that are on that grid
- Loop through the houses
- Create a dictionary of all distances from the house to the closest connected coordinate
- Add a path from the house to that coordinate
- Calculate the total distance of cables on the grid

#### Greedy constrained shared cables
- Get a copy of a grid of one of the districts
- Shuffle the list of houses that are on that grid
- Loop through the houses
- Create a dictionary of all distances from the house to the closest connected coordinate
- Add a path from the house to that coordinate if the battery connected to that coordinate is not full
- If battery is full, connect to another coordinate with a different battery
- If there are no more available batteries, mark as a failed attempt
- Calculate the total distance of cables on the grid

### Hillclimber algorithm
- Get a valid grid as input
- Make a copy of that grid
- Shuffle the list of houses on the grid
- Randomly select two houses from the grid
- Swap the cables for both houses if battery capacity allows it
- Check if the total cable length for the copy is smaller than the original
- If shorter, make the new copy the input for the next iteration
- If not shorter, go back to the previous situation
- Check total distance of cables on the grid

### Simulated Annealing algorithm
- Get a valid grid as input
- Make a copy of that grid
- Set a temperature that determines how much worse solutions the algorithm allows
- Shuffle the list of houses on the grid
- Randomly select two houses from the grid
- Swap the cables for both houses if battery capacity allows it
- Check if the total cable length for the copy is smaller than the original
- If shorter, make the new copy the input for the next iteration
- If not shorter, accept the new copy depending on the current temperature
- Update temperature a small step towards zero
- Check total distance of cables on the grid


## Structure of the repository
code
/algorithms: contains random, greedy, hillclimber, annealing and iterative algorithms
/classes: contains battery, cable, coordinate, grid and house classes
/visualisations: contains visualise functions

data
contains all data from the three districts

images
contains the images used in this README.md 

research_results
will contain all visualisations of all algorithms for all three districts after they have completed running

results
/not shared: contains the visualisation of a grid without shared cables after running
/shared cables: contains the visualisation of a grid with shared cables after running

main.py: code to run the programme
requirements.txt: contains all necessary packages for this programme


## Usage
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

Depending on your choices, you will get options for which algorithm and improvement algorithm you want to run. You will be prompted with the file path where you can find the visualisation of your algorithm result.