from collections import defaultdict
import xlrd

   
def BFS(graph,s,numOfVertex): 
  
    visited = [False] * (numOfVertex+1) #Initialize visited vertexs with indicated size
    queue = [] 
    queue.append(s) 
    visited[s] = True

    while queue: 
        s = queue.pop(0)  #Get head of queue
        print (s, end = " ") 
        for i in graph[s]:
            if  visited[i] == False: 
                queue.append(i) 
                visited[i] = True
    print("")
    
                
def DFS(graph, start,numOfVertex):
    
    visited = [False] * (numOfVertex+1) #Initialize visited vertexs with indicated size
    stack = []
    stack.append(start)
    visited[start] = True
    
    while stack:
        vertex = stack.pop() #Get tail of queue
        print (vertex, end = " ")
        for i in graph[vertex]:
            if  visited[i] == False: 
                stack.append(i)
                visited[i] = True      
                
                
#Read data to graph
workbook = xlrd.open_workbook("Graph_data.xls")
graph = defaultdict(list)
numOfVertex = 0;

for sheet in workbook.sheets():
    root = int(sheet.cell(0,1).value)
    for row in range(sheet.nrows):
        if row > 2:
            firstVertex = int(sheet.cell(row,0).value)
            secondVertex = int(sheet.cell(row,1).value)
            graph[firstVertex].append(secondVertex)
            if firstVertex > numOfVertex:
                numOfVertex = firstVertex
            if secondVertex > numOfVertex:
                numOfVertex = secondVertex
                
print("BFS: ",end = "")
BFS(graph,root,numOfVertex)
print("DFS: ",end = "")
DFS(graph,root,numOfVertex)