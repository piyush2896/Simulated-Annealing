from tour_manager import City, TourManager, Tour
from math import exp
import random


def acceptance_probability(energy, new_energy, temp):
    if new_energy < energy:
        return 1.0

    return exp((energy - new_energy) / temp)


def get_predefined_tour_manager():
    tm = TourManager()
    tm.add_city(City([60, 200]))
    tm.add_city(City([180, 200]))
    tm.add_city(City([80, 180]))
    tm.add_city(City([140, 180]))
    tm.add_city(City([20, 160]))
    tm.add_city(City([100, 160]))
    tm.add_city(City([200, 160]))
    tm.add_city(City([140, 140]))
    tm.add_city(City([40, 120]))
    tm.add_city(City([100, 120]))
    tm.add_city(City([180, 100]))
    tm.add_city(City([60, 80]))
    tm.add_city(City([120, 80]))
    tm.add_city(City([180, 60]))
    tm.add_city(City([20, 40]))
    tm.add_city(City([100, 40]))
    tm.add_city(City([200, 40]))
    tm.add_city(City([20, 20]))
    tm.add_city(City([60, 20]))
    tm.add_city(City([160, 20]))
    
    return tm

def simulated_annealing(temp, coolin_rate, tm):
    current_tour = Tour(tm)
    current_tour.generate_random_tour()
    
    print('Initial distance:', current_tour.get_distance())
    print('-'*80, '\n')
    
    best_tour = Tour(tm, current_tour.tour)
    
    while temp > 1:
        print('\nSystem State - Temp:', temp, '\tCooling rate:', coolin_rate, '\tCurrent best distance', best_tour.get_distance())
        new_tour = Tour(tm, current_tour.tour)
        
        tour_pos_1 = random.randint(0, len(new_tour.tour)-1)
        tour_pos_2 = random.randint(0, len(new_tour.tour)-1)
        
        new_tour.set_city(tour_pos_1, new_tour.tour[tour_pos_2])
        new_tour.set_city(tour_pos_2, new_tour.tour[tour_pos_1])
        
        curr_enegery = current_tour.get_distance()
        neigh_energy = new_tour.get_distance()
        
        if(acceptance_probability(curr_enegery, neigh_energy, temp) > random.random()):
            current_tour = new_tour

        if current_tour.get_distance() < best_tour.get_distance():
            best_tour = current_tour

        temp *= 1-coolin_rate

    print('\n', '-'*80)
    print('Final Solution Distance: ', best_tour.get_distance())
    print('Tour\n', best_tour)

if __name__ == '__main__':
    simulated_annealing(10000, 0.3, get_predefined_tour_manager())