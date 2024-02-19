from Solver import *

model = Model()
model.BuildModel()

# Initialize the solver with the built model
solver = Solver(model)

# Assuming Solver class has a method to solve the VRP
solution = solver.solve()  # This method needs to be implemented in Solver.py
