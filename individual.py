
import random
import pyrosim
import math
import numpy as np
# from robot import ROBOT
from minimalRobot import ROBOT

class INDIVIDUAL:
    def __init__(self, i):
        self.ID = i
        self.genome = np.random.random(4) *2 -1
        self.fitness = 0


    def Evaluate(self, pb):
        sim = pyrosim.Simulator(play_paused=False, eval_time=1000, play_blind=pb)
        robot = ROBOT(sim, self.genome)



        # run the simulationa
        sim.start()
        sim.wait_to_finish()

        # # x = sim.get_sensor_data(sensor_id=robot.P4, svi=0)
        y = sim.get_sensor_data(sensor_id=robot.P4, svi=1)
        # # z = sim.get_sensor_data(sensor_id=robot.P4, svi=2)
        # # print(y[-1])

        self.fitness = y[-1]
    def Start_Evaluation(self, pb):
        self.sim = pyrosim.Simulator(play_paused=False, eval_time=500, play_blind=pb)
        self.robot = ROBOT(self.sim, self.genome)
        self.sim.start()
    
    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)
        self.fitness = y[-1]
        del self.sim



    def Mutate(self):
        genToMutate = random.randint(0,3)
        self.genome[genToMutate] = random.gauss(self.genome[genToMutate], 
                                                math.fabs(self.genome[genToMutate] *0.99))

    def Print(self):
        print('[', self.ID,':',  self.fitness, '] ', end=' ')
        # print('['),
        # print(self.ID),
        # print(self.fitness),
        # print(' ]')

