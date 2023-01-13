
import pybullet as p
import time

physicsClint = p.connect(p.GUI)

for _ in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(_)
p.disconnect()