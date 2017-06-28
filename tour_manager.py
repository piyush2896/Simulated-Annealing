import numpy as np
import random


class City:

    def __init__(self, coords=None):
        if coords == None:
            self.coords = 250 * np.array(np.random.random_sample((1, 2)), astype('uint32')) + 50
        else:
            self.coords = np.array(coords)

    def distance_to_city(self, city):
        sq_abs_coords_diff = (np.abs(self.coords - city.coords))**2
        return np.sqrt(np.sum(sq_abs_coords_diff))

    def __str__(self):
        return '<' + str(self.coords[0]) + ', ' + str(self.coords[1]) + '>'


class TourManager:

    def __init__(self):
        self.cities = []
        self.num_of_cities = 0

    def add_city(self, city):
        self.cities.append(city)
        self.num_of_cities += 1

    def get_city(self, index):
        return self.cities[index]
    

class Tour:

    def __init__(self, tour_manager, tour=None):
        if tour != None:
            self.tour = tour
        else:
            self.tour = []
        self.tour_manager = tour_manager
        self.distance = 0

    def generate_random_tour(self):
        self.tour = self.tour_manager.cities
        random.shuffle(self.tour)

    def set_city(self, city_pos, city):
        self.tour[city_pos] = city
        self.distance = 0

    def get_distance(self):
        if self.distance == 0:
            tour_distance = 0
            for i in range(len(self.tour)):
                from_city = self.tour[i]
                if i < len(self.tour)-1:
                    dest_city = self.tour[i+1]
                else:
                    dest_city = self.tour[0]
                tour_distance += from_city.distance_to_city(dest_city)
            self.distance = tour_distance
        return self.distance

    def __str__(self):
        tour_str = " | "
        for i in self.tour:
            tour_str += str(i) + " | "
        return tour_str

