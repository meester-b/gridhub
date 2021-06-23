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
        # print(coord)
        x = coord[0]
        y = coord[1]
        cluster_path = [[x, y]]
        bat = self.grid.coordinates[self.grid.cols * self.grid.rows + int(x) - self.grid.rows * (int(y) + 1)].batteries[0]

        repeat = 0

        while repeat == 0:
            # for point in list of points connected to a battery
            for path in self.bat_houses[bat]:
                # print(path)
                # if this point is a house
                for point in path:
                    house = self.grid.coordinates[self.grid.cols * self.grid.rows + int(point[0]) - self.grid.rows * (int(point[1]) + 1)]

                    if house.houses:
                        # print(house)
                        if house.houses[0].path:
                        # for a piece in this house path
                            for x in house.houses[0].path:
                                # print(x)
                                # if this coordinate is 
                                if self.grid.coordinates[self.grid.cols * self.grid.rows + int(x[0]) - self.grid.rows * (int(x[1]) + 1)] == coord:
                                    # print(house, coord)
                                    list = []

                                    for item in house.houses[0].path:
                                        list.append(item)
                                        # print("Added to list")
                                        
                                    if list not in cluster_path:
                                        cluster_path.append(list)
                                        # print("Added to cluster path")
                                    else:
                                        repeat = 1
                                        # print("Repeated")

                            coord = self.grid.coordinates[self.grid.cols * self.grid.rows + int(x[0]) - self.grid.rows * (int(x[1]) + 1)]
                            # house = coord.houses[0]

        return cluster_path

    def path_is_better(self, path1, path2):
        if len(path1) > len(path2):
            return True
        return False

    def unconnect(self, path, bat):
        # print(path)
        for i in path:
            # print(i)
            # print(len(i))
            if len(i) > 2:
                for j in i:
                    # print(j)
                    coord = self.grid.coordinates[self.grid.cols * self.grid.rows + int(j[0]) - self.grid.rows * (int(j[1]) + 1)]
                    # print(coord)
                    # if coord.batteries:
                    #     coord.batteries.remove(bat)
                    if bat in coord.batteries:
                        # print(bat)
                        coord.batteries.remove(bat)
            else:
                coord = self.grid.coordinates[self.grid.cols * self.grid.rows + int(i[0]) - self.grid.rows * (int(i[1]) + 1)]
                if bat in coord.batteries:
                        # print(bat)
                        coord.batteries.remove(bat)
            

    def replace_path(self, path1, cluster_path, bat):
        # print(bat)
        self.unconnect(path1, bat)

        # print(cluster_path)
        # print(bat)

        for coord in cluster_path:
            # print(coord)
            ## BAT HIER IS OPEENS EEN LIST
            # print(bat)
            self.unconnect(cluster_path, bat)
        
        distances = {}

        for coord in self.bat_houses[bat]:
            print(f"Coord: {coord}")
            for x in coord:
                print(f"X: {x}")
                y = self.grid.coordinates[self.grid.cols * self.grid.rows + int(x[0]) - self.grid.rows * (int(x[1]) + 1)]
                for point in cluster_path:
                    print(f"point: {point}")
                    z = self.grid.coordinates[self.grid.cols * self.grid.rows + int(point[0]) - self.grid.rows * (int(point[1]) + 1)]
                    dist = self.grid.calc_distance(y, z)

                    ## MOMENTEEL ZIT DE FOUT HIER, JE MAG GEEN LSIT GEVEN ALS KEY
                    distances[[y, z]] = dist

        # DUS DAN MOET JE HIERMEE OOK EEN ANDERE MANIER BEDENKEN OM DE TWEE PUNTEN TERUG TE VINDEN
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
            pathnumber = 0
            # print(bat)
            for path in self.bat_houses[bat]:
                # print(self.bat_houses)
                # print(pathnumber)
                if self.is_long_path(path):
                    # print("Long path")
                    # print(path)
                    coord = self.find_house(path)
                    cluster_path = self.determine_cluster(coord)
                    # print(bat)
                    self.replace_path(path, cluster_path, bat)
                
                pathnumber += 1


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
