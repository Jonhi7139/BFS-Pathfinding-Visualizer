class BFS:
    def __init__(self,path):
        self.path=path
        self.visited=set(path[0])
        self.bestPath=None

    def goDown(self,limit,obs):
        patio=[]
        for i in self.path:
            k=True
            y=(i[-1][-1])+1
            p=i[-1][-2]
            if y>limit or (p,y)in self.visited or (p,y) in obs :
                k=False
            if(k):
                self.visited.add((p,y))
                xclone=i.copy() 
                xclone.append((p,y))
                patio.append(xclone)
        return patio
    
    def goUp(self,obs):
        patio=[]
        for i in self.path:
            k=True
            y=(i[-1][-1])-1

            p=i[-1][-2]        
            if y<0 or (p,y)in self.visited or (p,y) in obs:
                k=False
            if(k):
                self.visited.add((p,y))
                xclone=i.copy()
                xclone.append((p,y))
                patio.append(xclone)
        return patio
    def goRight(self,limit,obs):
        patio=[]
        for i in self.path:
            k=True
            y=i[-1][-1]
            p=i[-1][-2]+1
            if p>limit or (p,y)in self.visited or (p,y)in obs:
                k=False
            if(k):
                self.visited.add((p,y))
                xclone=i.copy()
                xclone.append((p,y))
                patio.append(xclone)
        return patio
    def goLeft(self,obs):
        patio=[]
        for i in self.path:
            k=True
            y=i[-1][-1]
            p=i[-1][-2]-1
            if p<0 or (p,y)in self.visited or (p,y)in obs:
                k=False
            if(k):
                self.visited.add((p,y))
                xclone=i.copy()
                xclone.append((p,y))
                patio.append(xclone)
        return patio
    def expand(self,limit,obs):
        down=self.goDown(len(limit)-1,obs)
        up=self.goUp(obs)
        right=self.goRight(len(limit[0])-1,obs)
        left=self.goLeft(obs)
        return down + up + right + left
    
    def check(self,y):
        for i in self.path:
            if i[-1]==y:
                self.bestPath=i


        