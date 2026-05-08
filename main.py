from MAPA.py import *
from BFS.py import *

map=Map(10,10)
map.generate()
Start=map.setStart()
Goal=map.setGoal()
map.draw()
bfs=BFS([[Start]])
while(bfs.path and bfs.bestPath==None):
    bfs.path=bfs.expand(map.grid,map.obs)
    bfs.check(Goal)
print(bfs.bestPath)




