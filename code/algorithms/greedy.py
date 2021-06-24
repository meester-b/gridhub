# Import copy and random.
import copy
import random

# import the grid class and the Random algorithm.
from code.classes import grid
from .random import Random

class Greedy(Random):
    """
    Greedy inherits the functions of Random.
    """

    def __init__(self, tries, district):
        super().__init__(tries, district)
        self.best_greedy_unc = None
        self.best_greedy_con = None
        self.best_try = None
        self.best_greedy_shared = None
        self.test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")

    def unconstrained_greedy(self):
        """
        Sums up all minimum distances from houses to batteries, without constraints.
        """
        
        # Make a deepcopy of the grid.
        grid = copy.deepcopy(self.test_grid)

        # Loop through the houses on the grid, pick the closest battery, add it and lay the cable.
        for house in grid.houses:
            bat = grid.pick_closest_battery(house)
            house.add_bat(bat)
            grid.lay_cable(bat, house)

        # Calculate distance and keep track of the total cable distance.
        grid.calc_dist()
        self.keep_track_greedy_unc(grid)

    def constrained_greedy(self):
        """
        Sums up all minimum distances from houses to batteries, without constraints.
        """ 

        # Keep track of try valid ratio.
        failed_attempts = 0
        valid_attempts = 0 

        # Keep track of variables across tries>
        min_sum_cables = 0
        total_dist = 0

        # Loop through the number of tries.
        for x in range(self.tries):
            # Make a deepcopy
            grid = copy.deepcopy(self.test_grid)

            # Shuffle the houses in the grid.
            random.shuffle(grid.houses)

            # Each try starts as valid.
            is_valid = True

            # Keep track of the cable length in the current try.
            sum_cables = 0

            # Loop through the houses on the grid.
            for house in grid.houses:
                # Check which batteries are still available for this house and append to list.
                for bat in grid.batteries:
                    dist = abs(house.y_coordinate - bat.y_coordinate) + abs(house.x_coordinate - bat.x_coordinate)

                    if house.output < bat.capacity_left:
                        house.available_bats[bat] = dist
                    else:
                        house.unavailable_bats[bat] = dist
                
                # Break out of the loop if there are no available batteries left.
                if not grid.bat_available(house):
                    super().false_try(grid)
                    is_valid = False
                    failed_attempts += 1
                    break

                # Get closest battery and its distance and lay cable from battery to the house.
                closest_battery = min(house.available_bats, key=house.available_bats.get)
                shortest_dist = house.available_bats.get(closest_battery)
                house.bats.append(closest_battery)
                closest_battery.houses.append(house)
                grid.lay_cable(closest_battery, house)

                # Subtract the output of the house from the remaining capacity of the battery.
                closest_battery.capacity_left -= float(house.output)             

                # Keep track of cable length per house and add to cable length of the try.
                sum_cables += shortest_dist

            # Count valid tries.
            if is_valid:
                valid_attempts +=1 

            # Count minimum and sum across tries.
            if is_valid:
                # First valid try is minimum and automatically the best try.
                if valid_attempts == 1:
                    min_sum_cables = sum_cables
                    self.best_try = grid
                    self.best_try.score = sum_cables

                # Update if a new try is better than the previous ties.
                if sum_cables < min_sum_cables:
                    min_sum_cables = sum_cables
                    self.best_try = grid
                    self.best_try.score = sum_cables

                # Add all cables to the total cable distance of the grid.
                total_dist += sum_cables
    
        # Print statistics.
        self.print_stats_greedy(total_dist, min_sum_cables, valid_attempts, failed_attempts)

        # Return best try.
        return self.best_try

    def keep_track_greedy_unc(self, grid):
        """
        Function that keeps track of greedy unconstrained algorithm tries.
        """

        if self.best_greedy_unc is None:
            self.best_greedy_unc = grid

    def keep_track_greedy_con(self, new_grid, best_grid):
        """
        Function that keeps track of greedy constrained algorithm tries.
        """

        if self.best_greedy_con is None:
            self.best_greedy_con = new_grid
        elif new_grid.score < best_grid.score:
            self.best_greedy_con = new_grid
    
    def print_stats_greedy(self, total_dist, min_sum_cables, valid_attempts, failed_attempts):
        """
        Function that prints the statistics.
        """

        if valid_attempts > 0:
            avg_dist = total_dist / valid_attempts
        else:
            avg_dist = 0
        
        print(f"\nThe shortest distance is {min_sum_cables}")
        print(f"The average distance is {avg_dist}\n")
        print(f"The number of valid attempts is {valid_attempts}")
        print(f"The number of failed attempts is {failed_attempts}")

    def run_unconstrained(self):
        """
        This function runs our unconstrained greedy algorithm.
        """

        self.unconstrained_greedy()
        return self.best_greedy_unc

    def run_constrained(self):
        """
        This function runs our constrained greedy algorithm.
        """

        self.constrained_greedy()
        if self.best_try is not None:
            return self.best_try
        else:
            print("No valid result found")

    def greedy_shared_unc(self):
        """
        Unconstrained greedy with shared cables (NOTE: with many runs it may run the baseline).
        """

        # loop for the number of tries
        for x in range(self.tries):
            # make deepcopy of houses and shuffle list
            grid = copy.deepcopy(self.test_grid) 
            grid.shuffle_list(grid.houses)      

            # loop through the houses on the grid
            for house in grid.houses:
                # make a list of distances 
                distances = {}
             
                # for every point on the connected coordinates cable line
                for point in grid.connected_coordinates:
                    # the key is the point object and the value the distance
                    distances[point] = grid.calc_distance(house, point)

                # get the minimum distance for every point
                connected_point = min(distances, key=distances.get)

                # calculate and add the path for visualisation
                path = grid.calc_path(house, connected_point)
                grid.add_path(path)

                # connect the battery with path
                grid.connect_power(path, connected_point.batteries[0])

            # calculate the length of the cable and keep track of best
            self.calc_cable_length(grid)
            self.keep_track_shared(grid, self.best_greedy_shared)
        
        # return the best try
        return self.best_greedy_shared

    def greedy_shared_con(self):
        """
        Constrained greedy with shared cables.
        """

        # Keep track of try valid ratio.
        failed_attempts = 0
        valid_attempts = 0 

        # Loop for the number of tries.
        for x in range(self.tries):
            # Make deepcopy and shuffle the list of grid houses (randomise)
            grid = copy.deepcopy(self.test_grid)
            grid.shuffle_list(grid.houses)      

            # Loop through the houses on the grid.
            for house in grid.houses:
                # Make a dict of distances.
                distances = {}
             
                # For every point on the connected coordinates cable line.
                for point in grid.connected_coordinates:
                    # Add the point to the distances dict if battery is available.
                    if not grid.bat_full(point, house): 
                        distances[point] = grid.calc_distance(house, point)

                # Keep track of failed attempts if it is not possible.
                if not distances:
                    super().false_try(grid)
                    failed_attempts += 1
                    break
            
                # Get the closest point and subtract house output from battery capacity.
                connected_point = min(distances, key=distances.get)
                connected_point.batteries[0].capacity_left -= house.output
                
                # Add a path between the house and the point, store it in house, and connect the path with power.
                path = grid.calc_path(house, connected_point)
                grid.add_path(path)
                house.path = path
                grid.connect_power(path, connected_point.batteries[0])
                
            # Calculate total score of the grid and add to valid attempts.
            self.calc_cable_length(grid)
            self.keep_track_shared(grid, self.best_greedy_shared)
            valid_attempts += 1
        
        # Return best shared.
        return self.best_greedy_shared


    def calc_cable_length(self, grid):
        """
        Calculate cable length.
        """

        sum = 0

        for point in grid.coordinates:
            for bat in point.batteries:
                sum += 1

        grid.score = sum

    def keep_track_shared(self, new_grid, best_grid):
        """
        Function that keeps track of greedy algorithm tries.
        """

        if self.best_greedy_shared is None:
            self.best_greedy_shared = new_grid
        elif new_grid.score < best_grid.score:
            self.best_greedy_shared = new_grid
    
    def run_shared_unc(self):
        """
        This function runs our unconstrained greedy algorithm
        """

        self.greedy_shared_unc()

        if self.best_greedy_shared is not None:
            print(f"The best try has a distance of {self.best_greedy_shared.score}")
            return self.best_greedy_shared
        else:
            print("No valid result found")

    def run_shared_con(self):
        """
        This function runs our constrained greedy algorithm
        """

        self.greedy_shared_con()
        
        if self.best_greedy_shared is not None:
            print(f"The best try has a distance of {self.best_greedy_shared.score}")
            return self.best_greedy_shared
        else:
            print("No valid result found")
