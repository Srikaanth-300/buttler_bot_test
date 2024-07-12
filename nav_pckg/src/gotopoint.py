#!/usr/bin/env python
import time
import argparse
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalID
from geometry_msgs.msg import Point, Quaternion

class nav_goal:
    def __init__(self):
        rospy.init_node('send_goal_node', anonymous=True)
        rospy.Subscriber('/move_base/cancel', GoalID, cancel_callback)
        self.home_position = [0,0,0,0,0,0,1]
        self.kitchen_position = [3.472,-4.016,0,0,0,0,1]
        self.table1_position = [5.155,4.251,0,0,0,0,1]
        self.table2_position = [-3.1,-3.198,0,0,0,0,1]
        self.table3_position = [-3.424,3.551,0,0,0,0,1]
        self.dict = {0:self.home_position, 1:self.table1_position, 2:self.table2_position, 3:self.table3_position, 4:self.kitchen_position}
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()
        self.confirmation_timeout = 5  # seconds
        self.order=[]

    def move_to_goal(self,id):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position = Point(id[0],id[1],id[2])
        goal.target_pose.pose.orientation = Quaternion(id[3],id[4],id[5],id[6])
        goal.id = id 
        self.client.send_goal(goal)
        self.client.wait_for_result()

    def cancel_callback(self,msg):
        cancel_id = msg.id
        order.remove(cancel_id)
        move_to_goal(order[id+1])
'''def send_goal(list):
    rospy.init_node('send_goal_node', anonymous=True)
    
    # Create an action client
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    
    # Wait until the action server has started up and started listening for goals
    client.wait_for_server()
    for x in range(len(list)):
    # Create a new goal to send to move_base
     goal = MoveBaseGoal()
     goal.target_pose.header.frame_id = "map"
     goal.target_pose.header.stamp = rospy.Time.now()
    
    # Set the goal point
     goal.target_pose.pose.position = Point(list[x][0],list[x][1],list[x][2])
     goal.target_pose.pose.orientation = Quaternion(list[x][3],list[x][4],list[x][5],list[x][6])

    # Send the goal
     client.send_goal(goal)
    
    # Wait for the result (success or failure)
     wait = client.wait_for_result()
     time.sleep(1)
    
    # Check the result
   # if not wait:
        #rospy.logerr("Action server not available!")
        #rospy.signal_shutdown("Action server not available!")
    #else:
    return client.get_result()'''

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="Parse multiple integers.")
        parser.add_argument('--tableno', type=int, nargs='+', required=True, help='A list of integer numbers')
        args = parser.parse_args()
        # Example goal point (x, y, z, qx, qy, qz, qw)
        order = (f'{args.tableno}')
        reach = nav_goal()
        #print(reach.dict[4])
        reach.move_to_goal(reach.dict[4])
        time.sleep(1)
        for x in range(len(order)):
            reach.move_to_goal(order[x])
            time.sleep(5)
        reach.move_to_goal(reach.dict[0])

        
        '''goal_points = [table_1,table_2,table_3,kitchen,home]
        result = send_goal(goal_points)
        if result:
            rospy.loginfo("Goal execution done!")'''
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
