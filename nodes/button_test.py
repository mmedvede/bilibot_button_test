#!/usr/bin/env python
import roslib; roslib.load_manifest('bilibot_button_test')
import rospy
from bilibot_node.msg import PowerboardSensorState
"""
  Example on how to use some of the bilibot's buttons.
  Check button status by doing 'rostopic echo sensor_state'
"""
rospy.init_node('button_test')

running = False

def loop(): 
  """
    Only move when running is True. 
    Value of running is derived from E-Stop and Demo button presses
  """
  if running:
    # Do some work here
    print "Doing something. Press E-Stop to stop."
  else:
    print "Not doing anything. Press demo to start."
    rospy.sleep(1)


def got_sensorstate(msg):
  # Press "Demo" button to start and "E-Stop" to stop
  global running
  if msg.demo_button:
    running = True
  if msg.estop_button:
    running = False

rospy.Subscriber('sensor_state', PowerboardSensorState, got_sensorstate) 

while not rospy.is_shutdown():
  loop()

#rospy.spin()
