import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length, width, height = 1, 1, 1
x ,y,z = 0, 0, 0.5

# length2, width2, height2 = 1, 1, 1
# x2 ,y2 ,z2 = 0, 1, 1.5

for i in range(10):
    for j in range(10):
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
            length, width, height = 0.9*length, 0.9*width, 0.9*height
            x, y, z = x , y, 0.9*z + 1.1
        length, width, height = 1, 1, 1
        x, y, z = x +1 , y, 0.5
    x, y, z = x, y+1, 0.5
# pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2], size=[length2,width2,height2])
pyrosim.End()