
import pyrosim
import matplotlib.pyplot as plt
import random
import copy
import pickle
from individual import INDIVIDUAL

# from robot import ROBOT
from minimalRobot import ROBOT
from population import POPULATION

# initiate sim

# parents = POPULATION(1)
# # print(parents.Evaluate())

# # exit()

# # print(parents.Print())


# for g in range(4000):
#     children = copy.deepcopy(parents)
#     children.Mutate()
#     children.Evaluate()
#     parents.ReplaceWith(children)
#     print(f'{g}, {parents.Print()}')

parent = INDIVIDUAL(1)
parent.Evaluate(True)
# print(parent.fitness)
for i in range(10000):

    child = copy.deepcopy(parent)
    child.Mutate()
    child.Evaluate(True)
    print("[g:",i,"]" ,"[pw:", parent.genome,"]" ,"[p:" , parent.fitness , "]", "[c:", child.fitness, "]")
    # print("genome:", parent.genome, child.genome)

    if (child.fitness > parent.fitness):
        parent = child
        child.Evaluate(False)

    with open('robot.p', 'wb') as f:
        pickle.dump(parent, f)


# # get data
# sensorData = sim.get_sensor_data(sensor_id= P2)
# # print(sensorData)


# # plot data
# f= plt.figure()
# panel = f.add_subplot(111)
# plt.plot(x)
# plt.plot(y)
# plt.plot(z)
# plt.show()
