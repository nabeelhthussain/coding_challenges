# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:07:10 2021

@author: nabeelhussain
"""

import unittest

def setup_graph():
    """
    This is the function that reads in the cities from a text file.
    Return:
    - graph : data structure containing cities
    """
    # Using readline()
    file1 = open('cities.txt', 'r')
    count = 0
    graph = {}
    
    while True:
        count += 1
     
        # Get next line from file
        line = file1.readline()
     
        # if line is empty
        # end of file is reached
        if not line:
            break
        line = line.replace('\n', '').replace(" ", "").split(',')
        i=0
        for city in line:
            if i == 0:
                prev_city = city
                i+=1
            else:
                if city in graph.keys():
                    graph[city] += [prev_city]
                else:
                    graph[city] = [prev_city]
                    
                if prev_city in graph.keys():
                    graph[prev_city] += [city]
                else:
                    graph[prev_city] = [city]


    file1.close()
    return graph

def isConnected(city1, city2, result, checked):
    """
    This is the function to calculate whether two cities are connected.
    Args:
    - city1 : name of city 1
    - city2 : name of city 2
    - result : initialized variable for the result
    - checked : list of cities that have been checked already ini the tree
    Return:
    - output : result (True or False)
    """
    city1 = city1.replace(" ", "")
    city2 = city2.replace(" ", "")
    graph = setup_graph()
    if city1 in graph.keys() and city2 in graph.keys():
        checked.append(city1)
        if city1 in graph[city2]:
            result = True
        elif city2 in graph[city1]:
            result = True
        else:
            #traverse
            for inter_city in graph[city1]:
                if inter_city not in checked:
                    checked.append(inter_city)
                    return isConnected(inter_city, city2, result, checked)
    else:
        print("Select a valid city")
        return False
    return result

class Tests(unittest.TestCase): #creating the class

    def test(self):  #method that tests the function 
        self.assertEqual(isConnected('Boston', 'Hartford', False, []),True) #testing by calling the function and passing the predicted result
        self.assertEqual(isConnected('Boston', 'NewYork', False, []),True)
        self.assertEqual(isConnected('Boston', 'Philadelphia', False, []),False)
        self.assertEqual(isConnected('Boston', 'Pittsburgh', False, []),False)
        self.assertEqual(isConnected('SanDiego', 'LosAngeles', False, []),True)
        self.assertEqual(isConnected('St.Petersburg', 'Tampa', False, []),True)
        self.assertEqual(isConnected('Boston', 'Tampa', False, []),False)

if __name__ == '__main__':
    unittest.main()