import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
planeId = p.loadURDF("D:/pythonProject/Pycharm/bullet3-master/examples/pybullet/gym/pybullet_data/plane.urdf")
cubeStartPos = [0, 0, 1]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
room = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/room.urdf", globalScaling=5, basePosition=cubeStartPos)
boxId = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/mir_ur.urdf")
boxId2 = p.loadURDF("C:/Users/Cat/Desktop/reveal_packages-master/industrial_arm/scenario/models/urdf/ur10-schunk-arm/model.urdf")
numJoints = p.getNumJoints(boxId)
for joint in range(numJoints):
    print(p.getJointInfo(boxId, joint))
p.setJointMotorControl(boxId, 23, p.VELOCITY_CONTROL, 10, 500)
p.setRealTimeSimulation(1)
while 1:
    time.sleep(1. / 240.)