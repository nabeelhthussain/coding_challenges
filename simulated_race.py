#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:07:10 2021

@author: nabeelhussain

"""
import random
import matplotlib.pyplot as plt

def get_rand_number(min_value, max_value):
    """
    This function gets a random number from a uniform distribution between
    the two input values [min_value, max_value] inclusively
    Args:
    - min_value (float)
    - max_value (float)
    Return:
    - Random number between this range (float)
    """
    range = max_value - min_value
    choice = random.uniform(0,1)
    return min_value + range*choice

def race_time(distance, accel):
    """
    This is the main function to calculate the race time.
    Args:
    - distance : input to function; must be in m
    Return:
    - output of function - Time
    """
    return ((2*distance)/accel)**0.5

def monte_carlo(num_samples, distance):
    """
    This is the main function to perform the monte carlo simulation.
    Args:
    - num_samples: number of similations to run
    - distance : input to function; must be in m
    Return:
    - output of function : number of wins for each type of vehicle
    """
    
    car_wins,motorbike_wins,truck_wins = 0,0,0

    for i in range(num_samples):
        
        #Get velocity for each vehicle
        v_car = get_rand_number(70, 100)
        v_motorbike = get_rand_number(55, 65)
        v_truck = get_rand_number(55, 65)
        
        #Get acceleration for each vehicle
        a_car = get_rand_number(5, 7)
        a_motorbike = get_rand_number(9.5, 11.5)
        a_truck = get_rand_number(2, 5)
        
        #Get drag coeffficient for each vehicle
        cd_car = get_rand_number(0.3, 0.7)
        cd_motorbike = get_rand_number(0.7, 1.1)
        cd_truck = get_rand_number(0.4, 0.8)
        
        # Calulate force of drag
        # Fdrag =  0.5 * Cd * A * rho * v2
        c = 0.00005
        rho = 1.29
        A_car = 2.2
        A_motorbike = 1
        A_truck = 2.8
        drag_car = c*cd_car*A_car*rho*(v_car**2)
        drag_motorbike = c*cd_motorbike*A_motorbike*rho*(v_motorbike**2)
        drag_truck = c*cd_truck*A_truck*rho*(v_truck**2)
        #print(drag_car,drag_motorbike, drag_truck)
        #Calculate time taken to finish the race for each vehicle
        time_car = race_time(distance, a_car*drag_car)
        time_motorbike = race_time(distance, a_motorbike*drag_motorbike)
        time_truck = race_time(distance, a_truck*drag_truck)
        
        
        if time_car < time_motorbike and time_car < time_truck:
            car_wins += 1
        elif time_motorbike < time_car and time_motorbike < time_truck:
            motorbike_wins += 1       
        else:
            truck_wins += 1     
    
    print("The Cars won ",car_wins, " times")
    print("The Motorbikes won ",motorbike_wins, " times")
    print("The Trucks won ",truck_wins, " times")

    return car_wins,motorbike_wins,truck_wins

if __name__ == '__main__':
    print("Simulating Races...")
    num_samples = 100000
    distance = 1000
    car_wins,motorbike_wins,truck_wins=monte_carlo(num_samples, distance) # (iterations, race distance in m)
    #plt.bar(["Car", "Motorbike", "Truck"],[car_wins,motorbike_wins,truck_wins])
    #plt.title("Number of Race Wins by Vehicle Type")
    #plt.ylabel("Race Wins")
