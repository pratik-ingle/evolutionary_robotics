from individual import INDIVIDUAL

class POPULATION:
    def __init__(self, popSize):
        self.p = {}
        for i in range(popSize):
            self.p[i] = INDIVIDUAL(i)
        # print(self.p)

    
    def Print(self):
        for i in self.p:
            self.p[i].Print()

    def Evaluate(self ):
        for i in self.p:
            # self.p[i].Evaluate(False)
            self.p[i].Start_Evaluation(False)
        
        for i in self.p:
            self.p[i].Compute_Fitness()
    
    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self, other):
        for i in self.p:
            if (self.p[i].fitness < other.p[i].fitness):
                self.p[i] = other.p[i]
