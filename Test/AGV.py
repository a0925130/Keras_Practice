import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
planeId = p.loadURDF("plane.urdf")
roomStartPos = [0, 0, 1]
obstacleSratPos_1 = [3.5, 2.5, 1]
obstacleSratPos_2 = [-3, 1, 1]
obstacleSratPos_3 = [3, -4, 1]
obstacleSratPos_4 = [6, 0, 1]
obstacleSratPos_5 = [-3, -4, 1]
obstacleSratPos_6 = [-5, -2, 1]

room = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/room.urdf", globalScaling=5, basePosition=roomStartPos)
obstacle_1 = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/obstacle.urdf", basePosition=obstacleSratPos_1)
obstacle_2 = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/obstacle.urdf", basePosition=obstacleSratPos_2)
obstacle_3 = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/obstacle.urdf", basePosition=obstacleSratPos_3)
obstacle_4 = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/obstacle.urdf", basePosition=obstacleSratPos_4)
obstacle_5 = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/obstacle.urdf", basePosition=obstacleSratPos_5)
obstacle_6 = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/obstacle.urdf", basePosition=obstacleSratPos_6)
boxId = p.loadURDF("C:/Users/Cat/Desktop/ur_mir_data/mir_ur.urdf")

numJoints = p.getNumJoints(boxId)
for joint in range(numJoints):
    print(p.getJointInfo(boxId, joint))
# p.getDynamicsInfo(planeId)
p.setJointMotorControl2(boxId, 19, p.POSITION_CONTROL, targetVelocity=10)

p.setRealTimeSimulation(1)
while 1:
    time.sleep(1. / 240.)