class Constraint:
    
    def __init__(self, leftVariable,rightVariable,equality):
        self.leftVariable = leftVariable   # 0 (x0)
        self.rightVariable = rightVariable # 1 (x1)
        self.equality = equality # True (=) False (!=)

def checkConstraints(variables,constraints):
    
    for i in range (len(constraints)):
        leftVariableIndex = constraints[i].leftVariable
        rightVariableIndex = constraints[i].rightVariable
        if constraints[i].equality and variables[leftVariableIndex] != variables[rightVariableIndex]:
            return False
        elif (not constraints[i].equality) and variables[leftVariableIndex] == variables[rightVariableIndex]:
            return False
    return True

############ Scenario 1 #############
c1 = Constraint(0,2,True) # (x0 = x2)
c2 = Constraint(1,3,False) # (x1 != x3)

A = [5,2,5,7] # Variables
B = [c1,c2] # Constraints

print("Scenario 1:",checkConstraints(A,B))

############ Scenario 2 #############

c1 = Constraint(0,2,True) # (x0 = x2)
c2 = Constraint(0,3,True) # (x0 = x3)

A = [5,2,5,7] # Variables
B = [c1,c2] # Constraints

print("Scenario 2:",checkConstraints(A,B))