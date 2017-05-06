import queue

#define the graph

r = [[0,1,1,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0],[0,0,0,0,0,1,1,0,0],
     [0,0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

#define the frontier queue
frontier = queue.Queue()

#put the starting node as 1
frontier.put(0)
explored=[]
target = 8

while(True):
    #pick the first element from the queue

    if(frontier.empty()):
        print("The target not found")
        break
    n= frontier.get()
    if (n in explored):
        continue
    explored.append(n)
    if (n==target):
        break
    #now get the child of n
    for i in range(0,9):

        if(r[n][i] == 1 and i not in explored):
             frontier.put(i)
print(explored)


