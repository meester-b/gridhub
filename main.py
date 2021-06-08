from code.algorithms import baseline
from code.classes import battery, house, cable, grid
# from code.visualisations import visualise as vis       
        
if __name__ == "__main__":
    district = "1"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
    
    # call algorithm 
    # baseline.unconstrained_baseline(100000)
    # baseline.constrained_baseline(100000)

    ## som van de minimale lengtes van ieder huis naar een batterij
    min_sum_cables = 0

    for houses in test_grid.houses:
        distances = []

        for batteries in test_grid.batteries:
            dist = abs(int(houses.y_coordinate) - int(batteries.y_coordinate)) + abs(int(houses.x_coordinate) - int(batteries.x_coordinate))
            distances.append(dist)

        shortest_dist = distances[0]

        for dist in distances:
            if dist < shortest_dist:
                shortest_dist = dist
        
        min_sum_cables += shortest_dist

    print(min_sum_cables)



    
