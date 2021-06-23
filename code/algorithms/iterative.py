import copy

from .greedy import Greedy

## in andere files gedaan:
# path opslaan in house
# house opslaan in coord en deze opslaan in bat

class Iterative(Greedy):
    """
    Improves a grid based without changing houses-battery combinations.
    The idea that this is the last step to improve pathing and decrease 
    the cable length. The concept might see a bit vague but it created in a way
    that older algo's dont need to be adjusted.
    """
    def __init__(self, grid):
        self.grid = grid
        self.bat_houses = {}

    def link_bat_houses(self, bat):
        list = []

        for coord in self.grid.coordinates:
            if bat in coord.batteries:
                if coord.houses:
                    list.append(coord.houses[0].path)

        self.bat_houses[bat] = list

    def is_long_path(self, path):
        if len(path) > 7:
            return True
        return False

    def find_house(self, path):
        for coord in path:
            if self.grid.coordinates[self.grid.cols * self.grid.rows + int(coord[0]) - self.grid.rows * (int(coord[1]) + 1)].houses:
                return coord 

    def determine_cluster(self, coord):
        print(coord)
        x = coord[0]
        y = coord[1]
        cluster_path = [[x, y]]
        bat = self.grid.coordinates[self.grid.cols * self.grid.rows + int(x) - self.grid.rows * (int(y) + 1)].batteries[0]

        repeat = 0

        while repeat == 0:
            # for point in list of points connected to a battery
            for point in self.bat_houses[bat]:
                # if this point is a house
                if point.houses:
                    # for a piece in this house path
                    for x in point.houses[0].path:
                        # if this coordinate is 
                        if self.grid.coordinates[self.grid.cols * self.grid.rows + int(x[0]) - self.grid.rows * (int(x[1]) + 1)] == coord:
                            list = []
                            for item in point.houses[0].path:
                                list.append(item)
                                
                            if list not in cluster_path:
                                cluster_path.append(list)
                            else:
                                repeat = 1

                            coord = self.grid.coordinates[self.grid.cols * self.grid.rows + int(x[0]) - self.grid.rows * (int(x[1]) + 1)]
                        # house = coord.houses[0]

        return cluster_path

    def path_is_better(self, path1, path2):
        if len(path1) > len(path2):
            return True
        return False

    def unconnect(self, path, bat):
        for i in range(len(path) - 1):
            self.grid.coordinates[self.grid.cols * self.grid.rows + int(path[i][0]) - self.grid.rows * (int(path[i][1]) + 1)].batteries.remove(bat)

    def replace_path(self, path1, cluster_path, bat):
        self.unconnect(path1)

        for coord in cluster_path:
            self.unconnect(cluster_path)
        
        distances = {}

        for coord in self.bat_houses[bat]:
            for point in cluster_path:
                dist = self.grid.calc_distance(coord, point)
                distances[[coord, point]] = dist

        shortest_dist = min(distances, key=distances.get)
        path2 = self.grid.calc_path(shortest_dist[0], shortest_dist[1])

        if self.path_is_better(path1, path2):  
            self.grid.connect_power(path2, bat)
            print(f"Improved by {len(path1)-len(path2)}")
        else:
            self.connect_power(path1, bat)

        self.connect_power(cluster_path, bat)
            

    def run(self):
        for bat in self.grid.batteries:
            self.link_bat_houses(bat)

        for bat in self.grid.batteries:
            for path in self.bat_houses[bat]:
                # print(self.bat_houses)
                if self.is_long_path(path):
                    # print(path)
                    coord = self.find_house(path)
                    cluster_path = self.determine_cluster(coord)
                    self.replace_path(path, cluster_path, bat)


        self.grid.keep_track_shared(self.best_greedy_shared, self.grid)
        print(self.best_greedy_shared.score)
    
        return self.best_greedy_shared

        




#### bat -----H-----H------H
####  |                     |
##### |---------------------H--H--H
            

    

        # for path in self.bat_houses[bat]:
        #     if len(path) > 5:

                    


    # for coords in grid.

# for x in range(self.tries):
# for house_coord in bat:
