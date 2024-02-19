import pandas as pd
import math


class Model:

# instance variables
    def __init__(self):
        self.allNodes = []
        self.customers = []
        self.matrix = []
        self.capacity = -1

    def BuildModel(self):
        depot = Node(0, 0, 50, 50)
        self.allNodes.append(depot)
        self.capacity = 200
        self.totalCustomers = 50
        self.customer_data = pd.read_excel('cust50.xlsx')


        for index, row in self.customer_data.iterrows():
            # Access the values for x, y, and dem from the current row
            x = row['x']
            y = row['y']
            dem = row['demand']
            cust = Node(index + 1, x, y, dem)
            self.allNodes.append(cust)
            self.customers.append(cust)

        # Clean the data and convert columns to the appropriate data types
        self.customer_data['id'] = self.customer_data['id'].astype(str).str.strip().astype(int)
        self.customer_data['x'] = self.customer_data['x'].astype(str).str.strip().astype(int)
        self.customer_data['y'] = self.customer_data['y'].astype(str).str.strip().astype(int)
        self.customer_data['demand'] = self.customer_data['demand'].astype(str).str.strip().astype(int)

        rows = len(self.allNodes)
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]

        for i in range(0, len(self.allNodes)):
            for j in range(0, len(self.allNodes)):
                a = self.allNodes[i]
                b = self.allNodes[j]
                dist = math.sqrt(math.pow(int(a.x) - int(b.x), 2) + math.pow(int(a.y) - int(b.y), 2))
                self.matrix[i][j] = dist

class Node:
    def __init__(self, idd, xx, yy, dem):
        self.x = xx
        self.y = yy
        self.ID = idd
        self.demand = dem
        self.isRouted = False

class Route:
    def __init__(self, dp, cap):
        self.sequenceOfNodes = []
        self.sequenceOfNodes.append(dp)
        self.sequenceOfNodes.append(dp)
        self.cost = 0
        self.capacity = cap
        self.load = 0