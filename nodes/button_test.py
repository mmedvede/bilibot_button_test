#!/usr/bin/env python
import roslib; roslib.load_manifest('bilibot_button_test')
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from bilibot_node.msg import PowerboardSensorState
"""
  Example on how to use some of the bilibot's buttons.
  Check button status by doing 'rostopic echo sensor_state'
"""
rospy.init_node('button_test')

pub = rospy.Publisher('cmd_vel', Twist)

running = False

def got_scan(msg): 
  """
    Only move when running is True. 
    Value of running is derived from E-Stop and Demo button presses
  """
  if running:
    # Do some work here
    cmd = Twist()
    cmd.linear.x = 0.1
    cmd.angular.z = 0
    pub.publish(cmd)
  else:
    # Send zero velocity command
    pub.publish(Twist())

def got_sensorstate(msg):
  # Press "Demo" button to start and "E-Stop" to stop
  global running
  if msg.demo_button:
    running = True
  if msg.estop_button:
    running = False

rospy.Subscriber('scan', LaserScan, got_scan)
rospy.Subscriber('sensor_state', PowerboardSensorState, got_sensorstate) 

rospy.spin()
