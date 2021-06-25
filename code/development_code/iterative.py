# Import Greedy
from .greedy import Greedy

class Iterative(Greedy):
    """
    Improves a grid based without changing houses-battery combinations.
    The idea that this is the last step to improve pathing and decrease 
    the cable length. The concept might seem a bit vague but it is created 
    in a way that earlier algorithms dont need to be adjusted.
    """

    def __init__(self, grid):
        self.grid = grid
        self.bat_houses = {}

    def link_bat_houses(self, bat):
        """
        Link battery to houses.
        """

        list = []

        for coord in self.grid.coordinates:
            if bat in coord.batteries:
                if coord.houses:
                    list.append(coord.houses[0].path)

        self.bat_houses[bat] = list

    def is_long_path(self, path):
        """
        Check if path is greater than 7.
        """

        if len(path) > 7:
            return True
        return False

    def find_house(self, path):
        """
        Find house with the coordinate in the path provided.
        """

        for coord in path:
            if self.grid.coordinates[self.grid.cols * self.grid.rows + int(coord[0]) - self.grid.rows * (int(coord[1]) + 1)].houses:
                return coord 

    def determine_cluster(self, coord):
        """
        Determine a cluster of houses.
        """

        x = coord[0]
        y = coord[1]
        cluster_path = [[x, y]]
        bat = self.grid.coordinates[self.grid.cols * self.grid.rows + int(x) - self.grid.rows * (int(y) + 1)].batteries[0]
        repeat = 0

        while repeat == 0:
            # for point in list of points connected to a battery
            for path in self.bat_houses[bat]:
                # if this point is a house
                for point in path:
                    house = self.grid.coordinates[self.grid.cols * self.grid.rows + int(point[0]) - self.grid.rows * (int(point[1]) + 1)]

                    if house.houses:
                        if house.houses[0].path:
                        # for a piece in this house path
                            for x in house.houses[0].path:
                                # if this coordinate is 
                                if self.grid.coordinates[self.grid.cols * self.grid.rows + int(x[0]) - self.grid.rows * (int(x[1]) + 1)] == coord:
                                    list = []

                                    for item in house.houses[0].path:
                                        list.append(item)
                                        
                                    if list not in cluster_path:
                                        cluster_path.append(list)
                                    else:
                                        repeat = 1

                            coord = self.grid.coordinates[self.grid.cols * self.grid.rows + int(x[0]) - self.grid.rows * (int(x[1]) + 1)]

        return cluster_path

    def path_is_better(self, path1, path2):
        """
        Determine if path is better than the previous path.
        """

        if len(path1) > len(path2):
            return True
        return False

    def unconnect(self, path, bat):
        """
        Unconnect path with battery.
        """

        for i in path:
            if len(i) > 2:
                for j in i:
                    coord = self.grid.coordinates[self.grid.cols * self.grid.rows + int(j[0]) - self.grid.rows * (int(j[1]) + 1)]
                    if bat in coord.batteries:
                        coord.batteries.remove(bat)
            else:
                print(i)
                coord = self.grid.coordinates[self.grid.cols * self.grid.rows + int(i[0]) - self.grid.rows * (int(i[1]) + 1)]
                if bat in coord.batteries:
                        coord.batteries.remove(bat)
            

    def replace_path(self, path1, cluster_path, bat):
        """
        Replace path.
        """

        self.unconnect(path1, bat)

        for coord in cluster_path:
            self.unconnect(cluster_path, bat)
        
        distances = {}

        for coord in self.bat_houses[bat]:
            for x in coord:
                y = self.grid.coordinates[self.grid.cols * self.grid.rows + int(x[0]) - self.grid.rows * (int(x[1]) + 1)]

                for point in cluster_path:                    
                    if len(point) > 2:
                        for k in point:
                            z = self.grid.coordinates[self.grid.cols * self.grid.rows + int(k[0]) - self.grid.rows * (int(k[1]) + 1)]
                    else:
                        z = self.grid.coordinates[self.grid.cols * self.grid.rows + int(point[0]) - self.grid.rows * (int(point[1]) + 1)]

                    dist = self.grid.calc_distance(y, z)
                    distances[[y, z]] = dist

        shortest_dist = min(distances, key=distances.get)
        path2 = self.grid.calc_path(shortest_dist[0], shortest_dist[1])

        if self.path_is_better(path1, path2):  
            self.grid.connect_power(path2, bat)
            print(f"Improved by {len(path1)-len(path2)}")
        else:
            self.connect_power(path1, bat)

        self.connect_power(cluster_path, bat)
            

    def run(self):
        """
        Runs the algorithm.
        """

        for bat in self.grid.batteries:
            self.link_bat_houses(bat)

        for bat in self.grid.batteries:
            for path in self.bat_houses[bat]:
                if self.is_long_path(path):
                    coord = self.find_house(path)
                    cluster_path = self.determine_cluster(coord)
                    self.replace_path(path, cluster_path, bat)


        self.grid.keep_track_shared(self.best_greedy_shared, self.grid)
        print(f"The improved score is now: {self.best_greedy_shared.score}")
    
        return self.best_greedy_shared
