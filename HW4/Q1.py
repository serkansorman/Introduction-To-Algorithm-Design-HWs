def getHotelSequences(stopPoints):
    SeqOfHotels = ""
    i = len(stopPoints)-1;
    while i >= 0:
        SeqOfHotels = str(i+1)+" "+SeqOfHotels
        i = stopPoints[i]-1
    return SeqOfHotels

def getMinPenalty(hotels):
    totalPenalty = [0] * len(hotels)
    stopPoints = [0] * len(hotels)
    for i in range(0,len(hotels)):
        totalPenalty[i] = pow(200 - hotels[i], 2) # Calculate penalty for each distance
        for j in range(0,i):
            nextPenalty = totalPenalty[j] + pow((200 - (hotels[i] - hotels[j])), 2)
            if  nextPenalty < totalPenalty[i]: # If current penalty < totalPenalty select this hotel to stop
                totalPenalty[i] = nextPenalty
                stopPoints[i] = j + 1     # Set stop point according to minimum penalty
    
    print("Sequence Of Hotels: ",getHotelSequences(stopPoints))
    print("Minimum Total Penalty: ",totalPenalty[len(hotels) - 1])
    

A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]
getMinPenalty(A)
        