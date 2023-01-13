import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length, width, height = 1, 1, 1
x ,y,z = 0, 0, 0.5

length2, width2, height2 = 1, 1, 1
x2 ,y2 ,z2 = 0, 1, 1.5

pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2], size=[length2,width2,height2])
pyrosim.End()