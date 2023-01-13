
import pybullet as p
import pybullet_data
import time


physicsClint = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeID  = p.loadURDF("plane.urdf")

p.loadSDF("box.sdf")

for _ in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(_)
p.disconnect()