# ASSIGNMENT PRBLEM USING BRANCH AND BOUND
!pip install gurobipy

from gurobipy import *

machines = ["M0", "M1", "M2", "M3"]
jobs = ["J0", "J1", "J2", "J3"]
I = range(len(machines))
J = range(len(jobs))

# Modified setup times matrix
Set_up_time = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [20, 30, 40, 50],
    [25, 35, 45, 55]
]

# Create a new model
m = Model("Assignment Model")

# Decision Variables
X = {}
for i in I:
    for j in J:
        X[i, j] = m.addVar(vtype=GRB.BINARY)

# Objective Function
m.setObjective(quicksum(Set_up_time[i][j] * X[i, j] for i in I for j in J), GRB.MINIMIZE)

# Constraints
for i in I:
    m.addConstr(quicksum(X[i, j] for j in J) <= 1)

for j in J:
    m.addConstr(quicksum(X[i, j] for i in I) >= 1)

# Optimize
m.optimize()

# Print Results
print("Optimized Set up Time:", m.objVal, "hours")
for i in I:
    print("-" * 30)
    print("Machine:", machines[i])
    print("-" * 30)
    for j in J:
        print("Jobs", jobs[j], X[i, j].x)
