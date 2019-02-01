
from collections import defaultdict

#Create graph using relations
def initGraph(peopleList,relations):
    graph = defaultdict(list)
    
    for i in peopleList:
        graph.setdefault(i,[])
        
    for person1, person2 in relations:
        graph[person1].append(person2)
        graph[person2].append(person1)
    return graph

def getInvitees(peopleList,relations):
    
    numOfPeople = len(peopleList)
    maxKnownPeople = len(peopleList) - 5
    graph = initGraph(peopleList,relations)
    removedPeople = []
    
    # First check whether each person knows at least five people and dont know
    # at least five people. if not, remove he/she from graph and add to 
    # removedPeoplelist
    for person in peopleList:
        if len(graph[person]) < 5 or len(graph[person]) > maxKnownPeople: 
            removedPeople.append(person)
            del graph[person]
            
    #Remove removed people from other people's relations list
    #And recheck remaining people provides indicated two constraints.
    #If not, remove person
    while(removedPeople):
        removedPerson = removedPeople.pop(0)
        for person in peopleList: 
            #Check people relations list contains removed person
            if removedPerson in graph[person]:
                graph[person].remove(removedPerson)
            #Recheck constraints after remove people
            if len(graph[person]) < 5 or len(graph[person]) > maxKnownPeople:
                del graph[person]

    return graph.keys() 
    
    
A = [0,1,2,3,4,5,6,7,8,9,10,11,12]

# (0,1) = (1,0) 
B = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), 
     (1, 2), (1, 3), (1, 4), (1, 5),
     (2, 3), (2, 4), (2, 5), 
     (3, 4), (3, 5), 
     (4,5),
     (6, 7), (6, 8), (6, 9), (6, 10), (6, 11),  # 6 Can not invite to party
     (8, 7), (8, 9), (8, 10), (8, 11), (8, 12)] # 8 Can not invite to party

print(getInvitees(A,B))