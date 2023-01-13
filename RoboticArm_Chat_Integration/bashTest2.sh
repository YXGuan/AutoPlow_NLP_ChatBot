#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1

source /home/yuxiang/interbotix_ws/devel/setup.bash
roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=px100 &
sleep 5 
python3 /home/yuxiang/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/examples/python_demos/arm_python_api_Test1.py &


# about $  (dollar sign)
# It tells the system to run the command in the background. From the bash man page on my system:
# If a command is terminated by the control operator &, 
# the shell executes the command in the background in a subshell. 
# The shell does not wait for the command to finish, and the return status is 0. 
# Commands separated by a ; are executed sequentially; the shell waits for each command to terminate in turn. 
# The return status is the exit status of the last command executed.

