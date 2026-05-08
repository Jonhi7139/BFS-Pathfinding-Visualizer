import random
class Map:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.grid=[[0 for i in range(self.width)]for t in range(self.height)]
        self.obs=set()

    def generate(self): 
        for t in range(self.height):
            for i in range(self.width):
                if random.random()<0.3:
                    self.grid[t][i]='#'
                    self.obs.add((t,i))
                else:
                    self.grid[t][i]='.'


    
    def draw(self):
        for i in range(self.height):
            print(" | ".join(self.grid[i]))

    def setStart(self):
        x=random.randint(0,self.width-1)
        y=random.randint(0,self.height-1)
        while (y,x) in self.obs:
            x=random.randint(0,self.width-1)
            y=random.randint(0,self.height-1)
        self.grid[y][x]="S"
        return(y,x)
    
    def setGoal(self):
        x=random.randint(0,self.width-1)
        y=random.randint(0,self.height-1)
        while (y,x) in self.obs or self.grid[y][x]=="S" :
            x=random.randint(0,self.width-1)
            y=random.randint(0,self.height-1)
        self.grid[y][x]="G"
        return(y,x)








