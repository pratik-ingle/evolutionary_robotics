
import pyrosim
import matplotlib.pyplot as plt
import random
from individual import INDIVIDUAL

from robot import ROBOT

# initiate sim
for i in range(0,10):

    individual = INDIVIDUAL()
    individual.Evaluate()   
    print(individual.fitness)

    

    

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

