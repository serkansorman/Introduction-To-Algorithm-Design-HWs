def getMinCost(n,M,NY,SF):
    
    minCostNY = [0] * n # minCostNY is the minimum costs for mont in NY
    minCostSF = [0] * n # minCostSF is the minimum costs for mont in SF
    
    # Set first month cost as a min cost for NY and SF
    minCostNY[0] = NY[0] 
    minCostSF[0] = SF[0]
    
    for i in range(1,n):
        # if the sum of move cost with the cost of other city is greater than 
        # the cost of current city, stay in the current city.
        minCostNY[i] = NY[i] + min(minCostNY[i-1],M+minCostSF[i-1])
        minCostSF[i] = SF[i] + min(minCostSF[i-1],M+minCostNY[i-1])
   
    return min(minCostNY[n-1],minCostSF[n-1]) # Get calculated total minimum cost

NY = [1,3,20,30]
SF = [50,20,2,4]

print("Total minimum cost:",getMinCost(4,10,NY,SF))