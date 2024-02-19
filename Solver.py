from VRP_Model import *
from SolutionDrawer import *


class Solution:
    def __init__(self):
        self.cost = 0.0
        self.routes = []


class Solver:
    def __init__(self, m):
        self.allNodes = m.allNodes
        self.customers = m.customers
        self.depot = m.allNodes[0]
        self.distanceMatrix = m.matrix
        self.capacity = m.capacity
        self.customer_data = m.customer_data
        self.totalCustomers = m.totalCustomers


    def solve(self):
        # Method to solve the VRP using the Nearest Neighbor Algorithm
        self.routes = self.nearest_neighbor_vrp(self.distanceMatrix, self.capacity, self.customer_data['demand'].tolist())
        self.calculate_total_cost()
        # Print the routes
        for index, route in enumerate(self.routes):
            print(f"Route {index + 1}: {route}")
        # Print the total cost
        print(f"Total cost: {self.cost}")



    def calculate_total_cost(self):
        # Placeholder for method to calculate the total cost of the routes
        total_cost = 0
        for route in self.routes:
            route_cost = 0
            for i in range(len(route) - 1):
                route_cost += self.distanceMatrix[route[i]][route[i + 1]]
                total_cost += route_cost
        self.cost = total_cost



    # Nearest Neighbor Algorithm for VRP
    def nearest_neighbor_vrp(self, distanceMatrix, capacity, demands):
        routes = []
        visited = set()
        #n = len(distanceMatrix)

        while len(visited) < self.totalCustomers:
            route = []
            current_capacity = 0
            current_location = 0  # depot is at index 0
            while True:
                visited.add(current_location)
                route.append(current_location)
                next_location = None
                min_distance = float('inf')
                for i in range(0, self.totalCustomers):
                    if i not in visited and current_capacity + demands[i] <= capacity:
                        if distanceMatrix[current_location][i] < min_distance:
                            min_distance = distanceMatrix[current_location][i]
                            next_location = i
                if next_location is None:  # No further customer can be added without exceeding capacity
                    break
                current_location = next_location
                current_capacity += demands[next_location]
            routes.append(route)
            if len(visited) == self.totalCustomers:  # All customers visited
                break
        return routes
