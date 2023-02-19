
import pyrosim
import matplotlib.pyplot as plt
import random

from robot import ROBOT

# initiate sim
for i in range(0,3):
    sim = pyrosim.Simulator(play_paused=False, eval_time=1000)

    robot = ROBOT(sim, random.random()*2 -1)


    # run the simulation
    sim.start()
    sim.wait_to_finish()


# # get data
# sensorData = sim.get_sensor_data(sensor_id= P2)
# # print(sensorData)



# # plot data
# f= plt.figure()
# panel = f.add_subplot(111)
# plt.plot(sensorData)
# plt.show()

