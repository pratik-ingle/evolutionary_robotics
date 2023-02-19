
import constants as c


class ROBOT:
    def __init__(self, sim, wts):

        self.send_objects(sim)
    #    self.send_joints(sim)
    #    self.send_sensors(sim)
    #    self.send_neurons(sim)
    #    self.send_synapses(sim,wts)

    def send_objects(self, sim):
        # create objects
        whiteObject = sim.send_cylinder(
            x=0, y=0, z=0.6, length=1.0, radius=0.1)
        redObject = sim.send_cylinder(
            x=0, y=0.5, z=1.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)
        # sim.send_cylinder(x=0, y=0, z=0.6, length=1.0 , radius=0.1 )
        # sim.send_cylinder(x=0, y=0.5, z=1.1, r=1, g=0, b=0, r1=0, r2=1, r3=0)
        O0 = sim.send_box(x=*, y=*, z=c.L + c.R, lenth=*, width=*, height=*, r=*, g=*, b=*)

    def send_joints(self, sim):
        # joint the hing
        joint = sim.send_hinge_joint(first_body_id=whiteObject, second_body_id=redObject,
                                     x=0, y=0, z=1.1, n1=-1, n2=0, n3=0, lo=-3.14159/2, hi=3.14159/2)

    def send_sensors(self, sim):
        # add sensors
        T0 = sim.send_touch_sensor(body_id=whiteObject)
        T1 = sim.send_touch_sensor(body_id=redObject)
        P2 = sim.send_proprioceptive_sensor(joint_id=joint)
        R3 = sim.send_ray_sensor(
            body_id=redObject, x=0, y=1.1, z=1.1, r1=0, r2=1, r3=0)
        self.P4 = sim.send_position_sensor(body_id=redObject)

    def send_neurons(self, sim):
        # sensory neurons
        SN0 = sim.send_sensor_neuron(sensor_id=T0)
        SN1 = sim.send_sensor_neuron(sensor_id=T1)
        SN2 = sim.send_sensor_neuron(sensor_id=P2)
        SN3 = sim.send_sensor_neuron(sensor_id=R3)
        MN2 = sim.send_motor_neuron(joint_id=joint)  # motor neuron

        sensorNeurons = {0: SN0, 1: SN1, 2: SN2, 3: SN3}
        motorNeuron = {0: MN2}

    def send_synapses(self, sim, wts):
        # # synapse
        # sim.send_synapse(source_neuron_id=SN0, target_neuron_id=MN2, weight=wt)
        # sim.send_synapse(source_neuron_id=SN1, target_neuron_id=MN2, weight=-1.0)
        # sim.send_synapse(source_neuron_id=SN2, target_neuron_id=MN2, weight=wt)
        # sim.send_synapse(source_neuron_id=SN3, target_neuron_id=MN2, weight=wt)

        for s, value in sensorNeurons.items():
            for m in motorNeuron:
                sim.send_synapse(source_neuron_id=value,
                                 target_neuron_id=motorNeuron[m], weight=wts[s])
